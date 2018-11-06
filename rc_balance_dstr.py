import os
import time

"""
https://github.com/StrawsonDesign/librobotcontrol
wget https://raw.githubusercontent.com/skankhunt-42/mr_blue_robot/master/rc_balance.c
git clone https://github.com/StrawsonDesign/librobotcontrol.git
cp ./librobotcontrol/examples/src/rc_balance.c ./librobotcontrol/examples/src/rc_balance.c.ORIGINAL
cp ./rc_balance.c ./librobotcontrol/examples/src/rc_balance.c
cd librobotcontrol
make
cp ./examples/bin/rc_balance /usr/bin/rc_balance_dstr
rc_balance_dstr -i dstr
"""


global turn_coefficient
turn_coefficient = 0.0175

global meter_coefficient
meter_coefficient = 14


global var_dir
var_dir = os.path.join(os.sep, "var", "lib", "cloud9", "BBBlue_DSTR")


print ("Make sure you have eduMPI balanced before running this script.")
print ("#rc_balance_dstr -i dstr")


def _create_cmd_file(cmd):
    global var_dir
    file_path = os.path.join(var_dir, cmd)
    open(file_path, 'a').close()


def move_forward(distance_meter = 1.0):
    global meter_coefficient
    print ("Moving forward")
    _create_cmd_file("up.txt.")
    time.sleep(meter_coefficient*distance_meter)
    _create_cmd_file("break.txt.")
    time.sleep(2)


def move_back(distance_meter = 1.0):
    global meter_coefficient
    print("Moving back")
    _create_cmd_file("down.txt.")
    time.sleep(meter_coefficient*distance_meter)
    _create_cmd_file("break.txt.")
    time.sleep(2)


def turn_left(degree = 90.0):
    global turn_coefficient
    print("Turning left")
    _create_cmd_file("left.txt.")
    time.sleep(turn_coefficient*degree)
    _create_cmd_file("break.txt.")
    time.sleep(2)


def turn_right(degree = 90.0):
    global turn_coefficient
    print("Turning right")
    _create_cmd_file("right.txt.")
    time.sleep(turn_coefficient*degree)
    _create_cmd_file("break.txt.")
    time.sleep(2)


def move_block():
    move_forward(0.28)


def spin_360():
    turn_left()
    turn_left()
    turn_left()
    turn_left()


def kitcken_lap():
    move_forward(1.2)
    turn_left()
    move_forward(2.1)
    turn_left()
    move_forward(1.2)
    turn_left()
    move_forward(2.1)
    turn_left()


def run_blocks():
    move_block()
    move_block()
    turn_left()
    move_block()
    move_block()
    turn_right()
    turn_right()
    move_block()
    move_block()
    turn_right()
    move_block()
    move_block()
    turn_right()
    turn_right()


run_blocks()

