import curses

from fallout_functions import slowWrite
from fallout_functions import centeredWrite
import fallout_login as login
import fallout_boot as boot
import fallout_hack as hack
import fallout_selection as select

################## text strings ######################

LOCKED_1 = 'ТЕРМИНАЛ ЗАБЛОКИРОВАН'
LOCKED_2 = 'ПОЖАЛУЙСТА СВЯЖИТЕСЬ С АДМИНИСТРАТОРОМ'
LOCKED_3 = 'OR FUCK YOUSELF'

################## global 'constants' ################

# amount of time to pause after lockout
LOCKED_OUT_TIME = 5000


################## functions #########################

def runLocked(scr):
    """
    Start the locked out portion of the terminal
    """
    curses.use_default_colors()
    size = scr.getmaxyx()
    width = size[1]
    height = size[0]
    # set screen to initial position
    scr.erase()
    curses.curs_set(0)
    scr.move(height // 2 - 3, 0)
    centeredWrite(scr, LOCKED_1)
    scr.move(height // 2 - 1, 0)
    centeredWrite(scr, LOCKED_2)
    scr.move(height // 2 + 1, 0)
    #centeredWrite(scr, LOCKED_3)
    #scr.refresh()
    curses.napms(LOCKED_OUT_TIME)


def beginLocked():
    """
    Initialize curses and start the locked out process
    """
    curses.wrapper(runLocked)
    pwd = hack.beginLogin()
    if pwd != None:
        login.beginLogin(False, 'ADMIN', pwd)
        print(select.beginSelection())
    else:
        beginLocked()

