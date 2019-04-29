import sklearn
import numpy as np
import pandas as pd
from scipy.optimize import least_squares


# Initial function
def f (x,y):
    #return np.sqrt((x+3* np.random.random())**2 + (y-2* np.random.random())**2)  + np.random.random()
    #return np.sqrt((x + 5) ** 2 + (y - 2) ** 2) + np.random.random()
    return np.log((x+3)**2 + (y+2)**2)


def f_wrapper(x):
    return f(x[0],x[1])

def return_minimal_paramemters():
    # Random point to start
    x_input = np.array([np.random.random(), np.random.random()])

    # Find minimum for current model
    minimum_parameters = least_squares(f_wrapper,x_input)['x']

    return minimum_parameters

# Evaluate the difference between the supplied parameters and the actual minimum
def evaluate_distance(x_input,min_params):



    return np.sqrt(np.sum(np.subtract(x_input,min_params)**2))

# Actual global minimum parameters
min_params = return_minimal_paramemters()

# Points where global minimum occured
z_min = f_wrapper(min_params)


def cost_function(input):
    return evaluate_distance(input, min_params)
