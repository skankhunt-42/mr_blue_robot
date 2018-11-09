import os
import time
import paramiko


global pw
pw = ""

#https://ozoblockly.com
global code_file
code_file = "ozoBlocklyProgram.ozocode"

global var_dir
var_dir = "/var/lib/cloud9/BBBlue_DSTR"


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


def main():
    global code_file
    global var_dir
    global pw

    stop_file = os.path.join(get_download_path(), "ozoblocky.txt.")

    code_folder = get_download_path()
    src_file = os.path.join(code_folder, code_file)
    dst_file = var_dir + "/" + code_file

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="beaglebone.local", username="root", password=pw)

    running = True
    while running:

        if os.path.isfile(src_file):
            print("Found new code on [%s]. Sending it to [%s]..." % (src_file, dst_file))
            ftp_client = ssh_client.open_sftp()
            ftp_client.put(src_file, dst_file)
            ftp_client.close()
            time.sleep(3)
            print("Code sent. Deleting [%s]..." % (src_file))
            os.remove(src_file)

        if os.path.isfile(stop_file):
            running = False

        time.sleep(1)

    print ("Done!")


main()
