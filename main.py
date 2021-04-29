import time
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np
import requests
from config import config_data


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
    screen = np.array(ImageGrab.grab(bbox=tuple(config_data["recognition_area"])))
    return screen


def recognition_text():
    text = pytesseract.image_to_string(take_screenshot(), lang=config_data['recognition_lang'])
    if text.strip():
        return text.strip()


def send_telegram(text: str):
    token = config_data['API_Token']
    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": config_data['channel_id'],
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")


def start(telegram=True, mouse_move=True, delay=5):
    while True:
        if telegram and mouse_move:
            if recognition_text() is not None:
                time.sleep(delay)
                send_telegram(recognition_text())
                move_mouse(tuple(config_data['string_coord']))
                double_click()
                move_mouse(tuple(config_data['print_coord']))
                click_left()
                time.sleep(delay)

            else:
                pass
        elif telegram and not mouse_move:
            if recognition_text() is not None:
                time.sleep(delay)
                send_telegram(recognition_text())
                time.sleep(delay)

            else:
                pass
        elif not telegram and mouse_move:
            if recognition_text() is not None:
                time.sleep(delay)
                move_mouse(tuple(config_data['string_coord']))
                double_click()
                move_mouse(tuple(config_data['print_coord']))
                click_left()
                time.sleep(delay)

            else:
                pass


