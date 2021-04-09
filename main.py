from PIL import Image
import pyautogui
import datetime

infile1 = 'Got_order.png'
infile2 = 'Empty_order.png'
pix_coord = (114, 231)


def compare_pixels(image1, image2, pixel_coordinates=(114, 231)):

    """image1, 2 - input opened images
        *pixel_coordinates - Tuple of  x, y comparing images """
    with Image.open(image1) as img1:
        with Image.open(image2) as img2:
            pix1 = img1.load()
            pix2 = img2.load()
    return pix1[pixel_coordinates] == pix2[pixel_coordinates]


def take_screenshot():
    screenshot = pyautogui.screenshot()
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    screenshot.save(timestamp + '.png')
    return timestamp + '.png'
