from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/whatsapp-status', methods=['POST'])
def whatsapp_status():
    data = request.json
    
    
    message_sid = data.get('Sid')
    status = data.get('Status')
    to_number = data.get('To')
    custom_data = data.get('CustomField')
    
    print(f"Update for {to_number}: Message {status} (ID: {message_sid})")
    
    if status == 'failed':
        error_code = data.get('ErrorCode')
        error_msg = data.get('ErrorMessage')
        print(f"Failure Reason: {error_msg} (Code: {error_code})")

    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)