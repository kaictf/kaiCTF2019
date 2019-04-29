from model import *

flag = "kaiCTF2019{m@chinE_Le@RN1nG_Is_c00l}"
wrong = "Too far. Try again"
threshhold = 1e-4

def evaluate_cost_func(x_coord, y_coord):

    input_x = np.array([x_coord,y_coord])

    distance = cost_function(input_x)

    return {"distance": distance}


def try_for_flag(x_coord, y_coord):
    user_z_coord = f(x_coord,y_coord)

    message = {"msg":"Blank answer"}

    # If user has found the coordinates for global minimum
    if np.abs(user_z_coord -z_min) <= threshhold:
        message['msg'] = flag
    else:
        message['msg'] = wrong

    return message



