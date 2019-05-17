from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)
PORT = 31339
HOST = '0.0.0.0'
PASSWORD = open('password.txt', 'r').read()


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['uname'] == "admin" and request.form['password'] == PASSWORD:
            return send_file("flag.txt", mimetype='text/html')
        else:
            return "Incorrect username/password. Hint: don't bruteforce, just be smart"
    else:
        return send_file("static/page.html", mimetype='text/html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
