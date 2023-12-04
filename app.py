from flask import Flask, jsonify
import random
import string
import base64
import hashlib
import os

app = Flask(__name__)

letters = string.ascii_letters + string.digits + string.punctuation


@app.route('/<int:pass_length>', methods=['GET'])
def generate_password(pass_length):
    if pass_length <= 0:
        return jsonify(error='Invalid password length'), 400

    password = ''.join(random.choice(letters) for _ in range(pass_length))
    base64_encoded = base64.b64encode(password.encode("utf-8")).decode()
    md5_encoded = hashlib.md5(password.encode('utf-8')).hexdigest()
    sha256_encoded = hashlib.sha256(password.encode('utf-8')).hexdigest()

    response = {
        'password': password,
        'encodings': {
            'base64': base64_encoded,
            'md5': md5_encoded,
            'sha256': sha256_encoded
        }
    }

    return jsonify(response)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
