from PIL import Image
import pyautogui
import datetime

infile1 = 'Got_order.png'
infile2 = 'Empty_order.png'
pix_coord = (114, 231)


def compare_pixels(image1, image2, pixel_coordinates):
    """image1, 2 - input images to compare
        *pixel_coordinates - tuple of  x, y pixels coordinates to compare
        returns False if images are different"""
    with Image.open(image1) as img1:
        with Image.open(image2) as img2:
            pix1 = img1.load()
            pix2 = img2.load()
    return pix1[pixel_coordinates] == pix2[pixel_coordinates]


def take_screenshot():
    """Save screenshot into current directory and
    returns str object of it name consists current date %H:%M:%S"""
    screenshot = pyautogui.screenshot()
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    screenshot.save(timestamp + '.png')
    return timestamp + '.png'
