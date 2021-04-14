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


#TODO TELEGRAM BOT!!!!!

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(open('README.md', 'r', encoding='utf-8').read())


def run_bot(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(response)


def main():
    """Start the bot."""
    updater = Updater(API, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, run_bot))
    updater.start_polling()
    updater.idle()