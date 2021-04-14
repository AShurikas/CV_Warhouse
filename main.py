import pyautogui
import datetime
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np


infile1 = 'Got_order.png'
infile2 = 'Empty_order.png'
pix_coord = (114, 231)
print_coord = (372, 143)
string_coord = (336, 206)
red_point_coord = (511, 209)


def click_left():
    pyautogui.leftClick()


def click_right():
    pyautogui.rightClick()


def move_mouse(coord):
    pyautogui.moveTo(coord)


def take_screenshot():
    """Returns img object of screenshot
    by coord area and save it in current directory by '%H%M' date format name"""
    filename = str(datetime.datetime.now().strftime('%H%M')) + '.png'
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
