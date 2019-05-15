from flask import Flask
from flask import request
from flask import make_response
import subprocess


app = Flask(__name__)
PORT = 80
HOST = '0.0.0.0'


index_page = """
<html>
<body>

<h2>Choose your option</h2>
<p><a href="/admin">Administrator options</a></p>
<p><a href="/feedback">Leave feedback</a></p>

</body>
</html>
"""


feedback_page = """
<html>
<body>

<h2>Feedback form</h2>
<p>Please leave your comment below. Our administrator will read it soon.</p>
<textarea rows="4" cols="80" name="comment" form="usrform">
</textarea>
<br>
<form action="" id="usrform" method="post">
  <input type="submit">
</form>

</body>
</html>
"""


blind_xss = ""


@app.route('/')
def index():
    return index_page


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        comment = request.form['comment']
        global blind_xss
        blind_xss = comment
        # print(comment)
        # gtimeout 10 /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --dump-dom http://127.0.0.1:5000/7a7e746699424921a611c1474df235b7
        cmd = "chromium-browser --headless --disable-gpu --disable-software-rasterizer --disable-dev-shm-usage --no-sandbox http://127.0.0.1:{}/7a7e746699424921a611c1474df235b7".format(str(PORT))
        # print(cmd)
        subprocess.call(cmd, shell=True, timeout=10)
        return 'Thanks for your feedback! We will review it soon.'
    else:
        return feedback_page


@app.route('/admin')
def admin():
    return "Hint: steal admin session"


@app.route('/7a7e746699424921a611c1474df235b7')
def secret():
    global blind_xss
    page = "<html><textarea>" + blind_xss + "</textarea></html>"
    # print(page)
    resp = make_response(page)
    resp.set_cookie('kaiCTF{c063c864e3fa3d802271ed5198f88118}')
    blind_xss = ""
    return resp


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
