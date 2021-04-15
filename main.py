import time
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np
import requests
from Tele_API import API_Token


string_coord = (336, 206)
print_coord = (372, 143)


def click_left():
    pyautogui.leftClick()


def double_click():
    pyautogui.doubleClick()


def click_right():
    pyautogui.rightClick()


def move_mouse(coord):
    pyautogui.moveTo(coord)


def take_screenshot():
    """Returns img object of screenshot
    by coord area"""
    screen = np.array(ImageGrab.grab(bbox=(185, 145, 293, 155)))
    return screen


def recognition_text():
    text = pytesseract.image_to_string(take_screenshot(), lang='rus')
    if text.strip():
        return text.strip()


def send_telegram(text: str):
    token = API_Token
    url = "https://api.telegram.org/bot"
    channel_id = "-513639392"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")


while True:
    if recognition_text() is not None:
        send_telegram(recognition_text())
        move_mouse(string_coord)
        double_click()
        move_mouse(print_coord)
        click_left()
        time.sleep(20)

    else:
        pass
