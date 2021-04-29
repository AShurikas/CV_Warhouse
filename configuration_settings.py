from PyQt6 import QtCore, QtGui, QtWidgets, QtTest
import clientui
import pyautogui
import json
from config import config_data


class set_configs(clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.pressed.connect(self.save_config)
        self.pushButton.pressed.connect(self.set_recognition_area)
        self.pushButton_3.pressed.connect(self.set_print_coord)
        self.pushButton_4.pressed.connect(self.set_string_coord)

    def set_API(self):
        if self.lineEdit.text():
            config_data['API_Token'] = self.lineEdit.text()

    def set_channel_id(self):
        if self.lineEdit_2.text():
            config_data['channel_id'] = self.lineEdit_2.text()

    def set_recognition_area(self, delay=5000):
        self.statusBar.clearMessage()
        self.textBrowser.clear()
        self.statusBar.showMessage('Fix mouse in the upper left corner of recognition area', delay)
        QtTest.QTest.qWait(delay)
        upper_corner = pyautogui.position()
        self.statusBar.showMessage('Fix mouse in the lower right corner of recognition area', delay)
        QtTest.QTest.qWait(delay)
        lower_corner = pyautogui.position()
        config_data['recognition_area'] = upper_corner + lower_corner
        self.textBrowser.append('Coordinates of recognition area set on ' + str(config_data['recognition_area']))

    def set_print_coord(self, delay=5000):
        self.statusBar.clearMessage()
        self.textBrowser.clear()
        self.statusBar.showMessage('Fix mouse in the print button area', delay)
        QtTest.QTest.qWait(delay)
        print_coord = pyautogui.position()
        config_data['print_coord'] = print_coord[:]
        self.textBrowser.append('Coordinates of print button set on ' + str(config_data['print_coord']))

    def set_string_coord(self, delay=5000):
        self.statusBar.clearMessage()
        self.textBrowser.clear()
        self.statusBar.showMessage('Fix mouse in the string area', delay)
        QtTest.QTest.qWait(delay)
        string_coord = pyautogui.position()
        config_data['string_coord'] = string_coord[:]
        self.textBrowser.append('Coordinates of string set on ' + str(config_data['string_coord']))

    def save_config(self):
        self.set_API()
        self.set_channel_id()
        config_json = json.dumps(config_data)
        configuration_file = 'config.py'
        with open(configuration_file, 'w', encoding='utf-8') as config_file:
            config_file.write('config_data = ' + config_json)
        self.textBrowser.clear()
        self.textBrowser.append(f'Configuration settings saved into {configuration_file}')


app = QtWidgets.QApplication([])
window = set_configs()
window.show()
app.exec()
