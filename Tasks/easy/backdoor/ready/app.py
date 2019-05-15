from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)
PORT = 80
HOST = '0.0.0.0'


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pwd = request.form['password']
        return 'Not implemented yet'
    else:
        return send_file("static/page.html", mimetype='text/html')


@app.route("/secret-link-123", methods=['GET', 'POST'])
def backdoor():
    if request.headers.get('User-Agent') == "backdoor_activated":
        return send_file("flag.txt", mimetype='text/html')
    else:
        return "Backdoor not activated"


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
