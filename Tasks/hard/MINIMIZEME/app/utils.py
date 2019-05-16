from model import *

flag = "kaiCTF{cc20bc619e6241f5c89ab014a379234a}"
wrong = "Too far. Try again"
threshhold = 0.20

def evaluate_cost_func(x_coord, y_coord):

    input_x = np.array([x_coord,y_coord])

    distance = cost_function_wrapper(input_x)

    return {"distance": distance}


def try_for_flag(x_coord, y_coord):
    user_z_coord = f(x_coord,y_coord)

    message = {"msg":"Blank answer"}

    # If user has found the coordinates for global minimum
    if np.abs(user_z_coord -z_min) <= threshhold:
        message['msg'] = flag
    else:
        message['msg'] = wrong
        message['poss'] = user_z_coord

    return message



