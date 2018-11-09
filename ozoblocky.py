import os
import time
import rc_balance_dstr
from xml.dom import minidom

#https://ozoblockly.com
global code_file
code_file = "ozoBlocklyProgram.ozocode"

global var_dir
var_dir = os.path.join(os.sep, "var", "lib", "cloud9", "BBBlue_DSTR")


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def execute_xml_code(xml):
    if os.path.isfile(xml):
        print(xml)
        xmldoc = minidom.parse(xml)
        itemlist = xmldoc.getElementsByTagName('block')
        #print(len(itemlist))
        #print(itemlist[0].attributes['type'].value)
        for s in itemlist:
            cmd = str(s.attributes['type'].value)
            cmd = cmd.replace("ozobot_newbie_", "")
            print(cmd)
            cmd_field = cmd.split("_")
            if len(cmd_field) > 2:
                if cmd_field[0] == "movement":
                    if cmd_field[1] == "forward":
                        # ozobot_newbie_movement_forward_1_step
                        step = int(cmd_field[2])
                        rc_balance_dstr.move_block(step)
                    if cmd_field[1] == "backward":
                        # ozobot_newbie_movement_backward_1_step
                        step = int(cmd_field[2]) * -1
                        rc_balance_dstr.move_block(step)
                    if cmd_field[1] == "speed":
                        step = 0
                        if cmd_field[2] == "medium":
                            # ozobot_newbie_movement_speed_medium
                            step = 2
                        if cmd_field[2] == "very":
                            # ozobot_newbie_movement_speed_very_fast
                            step = 5
                        rc_balance_dstr.move_block(step)
                    if cmd_field[1] == "turn":
                        if cmd_field[2] == "left":
                            # ozobot_newbie_movement_turn_left
                            rc_balance_dstr.turn_left(90.0)
                        if cmd_field[2] == "right":
                            # ozobot_newbie_movement_turn_right
                            rc_balance_dstr.turn_right(90.0)

                        if cmd_field[2] == "slight" and len(cmd_field) > 3:
                            if cmd_field[3] == "left":
                                # ozobot_newbie_movement_turn_slight_left
                                rc_balance_dstr.turn_left(45.0)
                            if cmd_field[3] == "right":
                                # ozobot_newbie_movement_turn_slight_right
                                rc_balance_dstr.turn_right(45.0)

                    if cmd_field[1] == "u":
                        if cmd_field[2] == "turn" and len(cmd_field) > 3:
                            if cmd_field[3] == "left":
                                # ozobot_newbie_movement_u_turn_left
                                rc_balance_dstr.turn_left(180.0)
                            if cmd_field[3] == "right":
                                # ozobot_newbie_movement_u_turn_right
                                rc_balance_dstr.turn_right(180.0)


def main():
    global code_file
    global var_dir

    #code_folder = get_download_path()
    code_file_full_path = os.path.join(var_dir, code_file)

    stop_file = os.path.join(var_dir, "ozoblocky.txt.")

    running = True
    while running:
        if os.path.isfile(code_file_full_path):
            execute_xml_code(code_file_full_path)
            time.sleep(1)
            os.remove(code_file_full_path)
        if os.path.isfile(stop_file):
            running = False

    print ("Done!")


main()

