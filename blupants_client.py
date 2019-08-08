import os
import time
import requests
import socket
import rc_balance_dstr
import blupants_car

global studio_url
studio_url = "http://flask-env.6xabhva87h.us-east-2.elasticbeanstalk.com"

global robot_id
robot_id = 0  # mr_blupants / eduMIP
robot_id = 1  # blupants_car

global step
step = 1

def execute_python_code(py):
    global step
    itemlist = str(py).split("\n")
    for s in itemlist:
        cmd = str(s)

        if s == "move_forward()":
            if robot_id == 0:
                rc_balance_dstr.move_block(step)
            if robot_id == 1:
                blupants_car.forward(step)
        if s == "move_backwards":
            if robot_id == 0:
                rc_balance_dstr.move_block(step)
            if robot_id == 1:
                blupants_car.backward(step)
        if s == "speed_up()":
            step += 1
            if robot_id == 0:
                rc_balance_dstr.move_block(step)
            if robot_id == 1:
                blupants_car.forward(step)
        if s == "turn_left()":
            if robot_id == 0:
                rc_balance_dstr.turn_left(90.0)
            if robot_id == 1:
                blupants_car.turn_left(90.0)
        if s == "turn_right()":
            if robot_id == 0:
                rc_balance_dstr.turn_right(90.0)
            if robot_id == 1:
                blupants_car.turn_right(90.0)
        if s == "turn_left(45)":
            if robot_id == 0:
                rc_balance_dstr.turn_left(45.0)
            if robot_id == 1:
                blupants_car.turn_left(45.0)
        if s == "turn_right(45)":
            if robot_id == 0:
                rc_balance_dstr.turn_right(45.0)
            if robot_id == 1:
                blupants_car.turn_right(45.0)
        if s == "turn_left(180)":
            if robot_id == 0:
                rc_balance_dstr.turn_left(180.0)
            if robot_id == 1:
                blupants_car.turn_left(180.0)
        if s == "turn_right(180)":
            if robot_id == 0:
                rc_balance_dstr.turn_right(180.0)
            if robot_id == 1:
                blupants_car.turn_right(180.0)


def get_local_ip():
    local_ip = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        local_ip = s.getsockname()[0]
    except:
        local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip


def get_code():
    url = studio_url + "/api/v1/code"
    code = {}
    local_ip = get_local_ip()
    params = dict(
        id=local_ip
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    # TODO change server to send the code type
    code = {"type": "python", "code": data}
    return code


def main():
    global code_file
    global var_dir

    running = True
    while running:
        print("Executing ...")
        code = get_code()
        time.sleep(2)
        if "type" in code:
            if code["type"] == "python":
                if "code" in code:
                    execute_python_code(code["code"])
        time.sleep(1)
        print("Done with executing!")
    print ("Done!")


main()

