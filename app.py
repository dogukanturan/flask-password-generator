from flask import Flask, render_template, request
import random
import base64
import hashlib

app = Flask(__name__)

html_headings = ("PASSWORD", "BASE-64", "MD5")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

@app.route('/')
def index():
    return """
            <h1>[Using]<h1>\n\t 
            <h2> /generate/length </h2>
            <h2> /generate/text </h2>\n\n
            <h1>[Example]<h1>\n\t 
            <h2> /generate/20 </h2> 
            <h2> /generate/hello </h2>"""

@app.route('/generate/<string:input>')
def generate(input):
    password = ""
    if input.isnumeric():
        for i in range(int(input)):
            password += random.choice(chars)
    else:
        password = input

    b64_encode = base64.b64encode(password.encode("utf-8"))
    md5_encode = hashlib.md5(password.encode('utf-8')).hexdigest()

    return render_template('index.html',
                           random_password=password,
                           base64_encoded_text = str(b64_encode, "utf-8"),
                           md5_encoded_text = md5_encode,
                           headings=html_headings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
