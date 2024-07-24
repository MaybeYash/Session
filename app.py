from flask import Flask, request, jsonify, render_template
from pyrogram import Client
import asyncio

app = Flask(__name__)

@app.route('/')
async def index():
    return render_template('index.html')

async def generate_session(api_id, api_hash, phone_number):
    async with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        session_string = await app.export_session_string()
        return session_string

@app.route('/generate_session', methods=['POST'])
async def generate_session_route():
    data = await request.get_json()
    api_id = data.get('api_id')
    api_hash = data.get('api_hash')
    phone_number = data.get('phone_number')
    
    if not api_id or not api_hash or not phone_number:
        return jsonify({'error': 'All fields are required'}), 400

    try:
        session_string = await generate_session(api_id, api_hash, phone_number)
        return jsonify({'string_session': session_string})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
