"""
password cracker program
"""
import os
import pyautogui
import time

try:
    passcodefile = open("10-million-password-list-top-1000000.txt", "r")
except:
    print("WE COULD NOT FIND OR OPEN PASSCODE FILE!!")
    time.sleep(5)
    quit()

time.sleep(5)
for password in passcodefile:
    password = password.replace("\n", "")
    cmd = f"unzip -P {password} secret.zip"
    #pyautogui.write(cmd, interval=0.1)
    #pyautogui.press('enter')
    #time.sleep(2)
    os.system(cmd)

