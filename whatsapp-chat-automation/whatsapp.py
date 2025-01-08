import pyautogui
from time import sleep

pyautogui.press('win')
pyautogui.write('WhatsApp', interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('09925126890', interval=0.1)
pyautogui.press('enter')
sleep(1)

for _ in range(100):
    #  1192, 996
    pyautogui.click(1192, 996)
    pyautogui.write('I', interval=0.1)
    pyautogui.press('enter')

    pyautogui.click(1192, 996)
    pyautogui.write('LoVe', interval=0.1)
    pyautogui.press('enter')

    pyautogui.click(1192, 996)
    pyautogui.write('YoU', interval=0.1)
    pyautogui.press('enter')

