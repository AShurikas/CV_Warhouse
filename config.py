from Xlib import display
import datetime


class Configs:
    def __init__(self, API_Token='', channel_id='', string_coord=(0,0),
                 print_coord=(0,0), recognition_area=(0,0), recognition_lang='rus', delay=5):
        self.API_Token = API_Token
        self.channel_id = channel_id
        self.string_coord = string_coord
        self.print_coord = print_coord
        self.recognition_area = recognition_area
        self.recognition_lang = recognition_lang
        self.delay = delay

    def set_API(self):
        self.API_Token = input('Input the Telegram Token, you register ---->>>>>')


    def set_channel_id(self):
        self.channel_id = input('Input the cahnnel_id of recepient ------>>>>>>')

    def set_string_coord(self, delay=5, warning_text='Fix the mouse on the string to take coord'):
        x1 = 0
        y1 = 0
        print(warning_text)
        while True:
            c = display.Display().screen().root.query_pointer()._data
            x = c["root_x"]
            y = c["root_y"]
            if x != x1 or y != y1:
                input_time = datetime.datetime.now()
                x1 = x
                y1 = y
            elif (x == x1) and ((datetime.datetime.now() - input_time).seconds > delay):
                self.string_coord = (x, y)

    def set_print_coord(self, delay=5, warning_text='Fix the mouse on the print area to take coord'):
        x1 = 0
        y1 = 0
        print(warning_text)
        while True:
            c = display.Display().screen().root.query_pointer()._data
            x = c["root_x"]
            y = c["root_y"]
            if x != x1 or y != y1:
                input_time = datetime.datetime.now()
                x1 = x
                y1 = y
            elif (x == x1) and ((datetime.datetime.now() - input_time).seconds > delay):
                self.print_coord(x, y)

    def set_recognition_area(self, delay=5):
        x1 = 0
        y1 = 0
        print('Fix the mouse cursor in the upper left corner of detecting area for 5 sec....')
        while True:
            c = display.Display().screen().root.query_pointer()._data
            x = c["root_x"]
            y = c["root_y"]
            if x != x1 or y != y1:
                input_time = datetime.datetime.now()
                x1 = x
                y1 = y
            elif (x == x1) and ((datetime.datetime.now() - input_time).seconds > delay):
                recognition_area_up = (x, y)
                print(x, y)
                x3 = 0
                y3 = 0
                print('Fix the mouse cursor in the lower right corner of detecting area for 5 sec....')
                while True:
                    c = display.Display().screen().root.query_pointer()._data
                    x2 = c["root_x"]
                    y2 = c["root_y"]
                    if x2 != x3 or y2 != y3:
                        input_time = datetime.datetime.now()
                        x3 = x2
                        y3 = y2
                    elif (x2 == x3) and ((datetime.datetime.now() - input_time).seconds > delay):
                        print(x2, y2)
                        self.recognition_area = recognition_area_up + (x2, y2)
                        return self.recognition_area

    def set_recognition_lang(self):
        self.recognition_lang = input('Input language of the target text to recognize ------->>>>>')
