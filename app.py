from flask import Flask, request, jsonify
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

app = Flask(__name__)

api_id = '29400566'
api_hash = '8fd30dc496aea7c14cf675f59b74ec6f'

@app.route('/generate_session', methods=['POST'])
def generate_session():
    phone_number = request.json.get('phone_number')
    
    if not phone_number:
        return jsonify({'error': 'Phone number is required'}), 400
    
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        client.start(phone=phone_number)
        session_string = client.session.save()
        return jsonify({'string_session': session_string})

if __name__ == '__main__':
    app.run(debug=True)
