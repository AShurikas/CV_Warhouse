import time
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np
import requests
import cv2
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
    input_image = take_screenshot()
    grey_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(grey_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(grey_image, lang=config_data['recognition_lang'])
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
            if isinstance(recognition_text(), str) and len(recognition_text() > 0):
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
            if isinstance(recognition_text(), str) and len(recognition_text() > 0):
                time.sleep(delay)
                send_telegram(recognition_text())
                time.sleep(delay)

            else:
                pass
        elif not telegram and mouse_move:
            if isinstance(recognition_text(), str) and len(recognition_text() > 0):
                time.sleep(delay)
                move_mouse(tuple(config_data['string_coord']))
                double_click()
                move_mouse(tuple(config_data['print_coord']))
                click_left()
                time.sleep(delay)

            else:
                pass


time.sleep(5)
start()
