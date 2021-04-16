import time
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np
import requests
from config import API_Token
from config import channel_id


string_coord = (336, 206)
print_coord = (372, 143)
recognition_area = (185, 145, 293, 155)
recognition_lang = 'rus'


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
    screen = np.array(ImageGrab.grab(bbox=recognition_area))
    return screen


def recognition_text():
    text = pytesseract.image_to_string(take_screenshot(), lang=recognition_lang)
    if text.strip():
        return text.strip()


def send_telegram(text: str):
    token = API_Token
    url = "https://api.telegram.org/bot"
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
        time.sleep(5)
        send_telegram(recognition_text())
        move_mouse(string_coord)
        double_click()
        move_mouse(print_coord)
        click_left()
        time.sleep(10)

    else:
        pass
