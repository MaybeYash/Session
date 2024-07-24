from flask import Flask, request, jsonify, render_template
from pyrogram import Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_session', methods=['POST'])
def generate_session():
    api_id = request.json.get('api_id')
    api_hash = request.json.get('api_hash')
    phone_number = request.json.get('phone_number')

    if not api_id or not api_hash or not phone_number:
        return jsonify({'error': 'All fields are required'}), 400

    try:
        app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)
        app.start()
        session_string = app.export_session_string()
        app.stop()
        return jsonify({'string_session': session_string})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
