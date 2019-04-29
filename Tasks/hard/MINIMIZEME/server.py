import flask
from flask import abort
from utils import  evaluate_cost_func, try_for_flag
import re
import numpy as np
from model import min_params

app = flask.Flask(__name__)

def check_for_float(*args):
    if all( re.match("^\d+?\.\d+?$", f) for f in args):
        return True
    return False

@app.route('/diff/<float(signed=True):x>/<float(signed=True):y>')
def ask_for_cost(x,y):
    print("Current parameters are: {}. Got: [{},{}]".format(min_params, x, y))
    if True or check_for_float(x,y):
        x, y   = float(x), float(y)
        ret = evaluate_cost_func(x,y)
        return flask.jsonify(ret)
    abort(404)


@app.route('/try/<float(signed=True):x>/<float(signed=True):y>')
def ask_for_flag(x,y):
    print("Current parameters are: {}. Got: [{},{}]".format(min_params, x,y))
    if True or check_for_float(x,y):
        x, y   = float(x), float(y)
        ret = try_for_flag(x,y)
        return flask.jsonify(ret)
    abort(404)


if __name__ == '__main__':

    app.run("0.0.0.0", 10000, debug=False,threaded=True)

