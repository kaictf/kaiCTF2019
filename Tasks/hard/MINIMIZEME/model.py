import sklearn
import numpy as np
import pandas as pd
from scipy.optimize import least_squares

# hyperparams
a = np.random.random()
b = np.random.random()
c = np.random.random()


# Initial function
def f (x,y):

    return np.log((x-a)**2 + (y+b)**2) +c



def f_wrapper(x):
    return f(x[0],x[1])

def return_minimal_paramemters():
    # Random point to start
    x_input = np.array([np.random.random(), np.random.random()])

    # Find minimum for current model
    minimum_parameters = least_squares(f_wrapper,x_input)['x']

    return minimum_parameters

# Evaluate the difference between the supplied parameters and the actual minimum
def cost_function(x_input,min_params):

    # Calculate function based on user's input
    z_user = f_wrapper(x_input)
    z_min = f_wrapper(min_params)

    # Calculate differenece between natural minipoint and user's suggested minimum
    cost = np.sqrt(np.sum(np.subtract(z_user, z_min) ** 2))


    return cost

# Actual global minimum parameters
min_params = return_minimal_paramemters()

# Points where global minimum occured
z_min = f_wrapper(min_params)


def cost_function_wrapper(input):
    return cost_function(input, min_params)
