from flask import Flask, request, jsonify
import paramiko
import uuid

app = Flask(__name__)

sessions = {}

@app.route('/ssh/connect', methods=['POST'])
def connect_ssh():
    data = request.json
    hostname = data.get('hostname')
    port = data.get('port', 22)
    username = data.get('username')
    password = data.get('password')
    private_key = data.get('privateKey')

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if private_key:
            pkey = paramiko.RSAKey.from_private_key(private_key)
            client.connect(hostname, port=port, username=username, pkey=pkey)
        else:
            client.connect(hostname, port=port, username=username, password=password)
        
        session_id = str(uuid.uuid4())
        sessions[session_id] = client
        return jsonify({'sessionId': session_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/ssh/execute', methods=['POST'])
def execute_command():
    data = request.json
    session_id = data.get('sessionId')
    command = data.get('command')

    client = sessions.get(session_id)
    if not client:
        return jsonify({'error': 'Invalid sessionId'}), 404

    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        return jsonify({'output': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/ssh/disconnect', methods=['POST'])
def disconnect_ssh():
    data = request.json
    session_id = data.get('sessionId')

    client = sessions.pop(session_id, None)
    if not client:
        return jsonify({'error': 'Invalid sessionId'}), 404

    try:
        client.close()
        return jsonify({'message': 'SSH connection closed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
