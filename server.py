from flask import Flask, request, jsonify
import hashlib
import base64

app = Flask(__name__)

# Chiave segreta e messaggio originale
SECRET_KEY = b'secret_key'
ORIGINAL_DATA = b'original_data'

# Calcola l'hash originale usando SHA-1
original_hash = hashlib.sha1(SECRET_KEY + ORIGINAL_DATA).hexdigest()

@app.route('/init', methods=['GET'])
def init():
    print(f"""Data Sent
Original hash: {original_hash}
Original data: {ORIGINAL_DATA.decode()}
{'-'*94}""")
    return jsonify({
        'original_hash': original_hash,
        'original_data': base64.b64encode(ORIGINAL_DATA).decode('ascii')
    })

@app.route('/verify', methods=['POST'])
def verify():
    data = base64.b64decode(request.form['data'])
    received_hash = request.form['hash']
    
    # Calcola l'hash per i dati ricevuti usando SHA-1
    calculated_hash = hashlib.sha1(SECRET_KEY + data).hexdigest()
    
    print(f"""Data: {data}
Received hash: {received_hash}
Calculated hash: {calculated_hash}
{'-'*94}""")    

    if calculated_hash == received_hash:
        return jsonify({'status': 'success', 'message': 'Data is valid!'})
    else:
        return jsonify({'status': 'failure', 'message': 'Invalid data or hash!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

