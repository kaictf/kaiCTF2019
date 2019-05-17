import flask
from flask import  render_template, url_for, request, jsonify, send_from_directory,send_file
import subprocess

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return send_file('index.html')

@app.route("/ping", methods=["POST"])
def ping():
    data = request.data
    ip = data.decode()

    if "nc" in ip:
        return jsonify({"result":"You're on the rigth way! But... if there are any other ways to send data through tcp/udp on linux?"})

    if not any([r in ip for r in (';',"nc", "socat", "apt", "apt-get", "&&")]):
        try:
            result = subprocess.check_output("ping -c 1 " + ip,
                                             stderr=subprocess.PIPE, shell=True, timeout=1)
            return jsonify({"result": "success"})
        except:
            pass
    return jsonify({"result": "error"})


@app.route("/static/<path:path>", methods=['GET'])
def server_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':

    app.run("0.0.0.0", 80)
