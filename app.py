from flask import Flask, render_template, jsonify
import random
import string
import base64
import hashlib

app = Flask(__name__)

html_headings = ("PASSWORD", "BASE64", "MD5")
letters = string.ascii_letters + string.digits + string.punctuation

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/generate/<string:input>')
def generate(input):
    if input.isnumeric():
        for i in range(int(input)):
            password = ''.join(random.choice(letters) for i in range(int(input)))
    else:
        password = input
    base64_encoded = base64.b64encode(password.encode("utf-8"))
    md5_encoded = hashlib.md5(password.encode('utf-8')).hexdigest()
    return render_template('index.html', random=str(password), base64_encoded=str(base64_encoded,"utf-8"), md5_encoded=md5_encoded, headings=html_headings)

@app.route('/api/<string:input>', methods=['POST'])
def api(input):
    if input.isnumeric():
        for i in range(int(input)):
            password = ''.join(random.choice(letters) for i in range(int(input)))
    else:
        password = input
    base64_encoded = base64.b64encode(password.encode("utf-8"))
    md5_encoded = hashlib.md5(password.encode('utf-8')).hexdigest()
    return jsonify(random=str(password), base64_encoded=str(base64_encoded), md5_encoded=str(md5_encoded))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)