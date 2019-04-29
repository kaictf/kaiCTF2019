import requests
import sklearn
import numpy as np
import pandas as pd
from scipy.optimize import least_squares,minimize,fmin_cg



diff_link = "http://127.0.0.1:10000/diff/{0:.10f}/{0:.10f}"
flag_link = "http://127.0.0.1:10000/try/{0:.10f}/{0:.10f}"

def get_cost_evaluation(x_,y_):

    actual_link= diff_link.format(x_,y_)
    ans = requests.get(actual_link).json()

    return ans['distance']

def get_flag_for_position(x_,y_):

    actual_link = flag_link.format(x_, y_)
    ans = requests.get(actual_link).json()

    return ans

def get_c_eval_wrapper(x):
    cost = get_cost_evaluation(x[0],x[1])
    #print(x, cost)
    return cost


eta0 = np.array([np.random.random(),np.random.random() ])

#minimum_parameters = minimize(get_c_eval_wrapper, eta0, method='Nelder-Mead', tol=1e-6)
minimum_parameters = minimize(get_c_eval_wrapper, eta0, tol=1e-6)['x']
#fmin_cg

flag = get_flag_for_position(*minimum_parameters)

print(flag)
print(minimum_parameters)