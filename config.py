class Configs:
    def __init__(self, API_Token, channel_id, string_coord,
                 print_coord, recognition_area, recognition_lang):
        self.API_Token = API_Token
        self.channel_id = channel_id
        self.string_coord = string_coord
        self.print_coord = print_coord
        self.recognition_area = recognition_area
        self.recognition_lang = recognition_lang

    def set_API(self):
        self.API_Token = input('Input the Telegram Token, you register ---->>>>>')

    def set_channel_id(self):
        self.channel_id = input('Input the cahnnel_id of recepient ------>>>>>>')

    def set_string_coord(self):






