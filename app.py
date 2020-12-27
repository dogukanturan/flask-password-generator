from flask import Flask
from flask import render_template
import random
import base64
import hashlib

app = Flask(__name__)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

@app.route('/')
def index():
    return "<h3> /generate/pass-length </h3>"

@app.route('/generate/<string:id>')
def generate(id):
    password = ''
    for i in range(int(id)):
        password += random.choice(chars)

    b64_encode = base64.b64encode(password.encode("utf-8"))
    md5_encode = hashlib.md5(password.encode('utf-8')).hexdigest()

    return render_template('index.html', 
                            random_password=password, 
                            base64_encoded_text = str(b64_encode, "utf-8"), 
                            md5_encoded_text = md5_encode)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)