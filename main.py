import pyautogui
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
from Tele_API import API_Token as API


def click_left():
    pyautogui.leftClick()


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


if recognition_text() is not None:
    pass
else:
    pass
