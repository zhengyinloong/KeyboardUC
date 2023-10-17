# -*- coding:utf-8 -*-
# test_keyboard_remapper.py in KeyboardUC
# zhengyinloong
# 2023/10/5

import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFontDialog, QFileDialog, QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtCore

from remapper import Ui_Subui_KeyboardLayout
from config.settings import *


class Sub_Remap(QWidget, Ui_Subui_KeyboardLayout):
    def __init__(self):
        super(Sub_Remap, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================
        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.resize(UI_WIDTH, UI_HEIGHT)

        # buttons init
        for bt_number in range(len(self.groupBox_Keyboard.children()[1:])):
            self.groupBox_Keyboard.children()[1 + bt_number].keyNumber = bt_number
            self.groupBox_Keyboard.children()[1 + bt_number].keyCode = None
            # self.groupBox_Keyboard.children()[1 + bt_number].setText('None')
        # keyboard_map
        self.Map = {}
        self.ReadMap()

        self.currentPressedKey = self.pushButton_1
        self.currentPressedKey.setStyleSheet('QPushButton{background:#f7acbc;}')
        self.lineEdit_KeyNumber.setText(str(self.currentPressedKey.keyNumber))
        self.lineEdit_KeyCode.setText(str(self.currentPressedKey.keyCode))

        self.comboBox_KeyName.addItems(KEY_NAMES)

    def CallBackFunctions(self):
        # key
        for bt in self.groupBox_Keyboard.children()[1:]:
            bt.clicked.connect(lambda _, button=bt: self.PressKey(button))
            bt.number = bt.objectName()
        # button
        self.pushButton_Save.clicked.connect(self.SaveKeys)
        # lineEdit
        # self.lineEdit_KeyCode.textChanged.connect(self.RemapKey)
        # self.comboBox_KeyName.currentTextChanged.connect(self.RemapKey2)
        self.comboBox_KeyName.textActivated.connect(self.RemapKey2)

    def PressKey(self, button):
        self.currentPressedKey.setStyleSheet('QPushButton{background:#ffffff;}')
        self.currentPressedKey = button
        self.currentPressedKey.setStyleSheet('QPushButton{background:#f7acbc;}')
        # print(self.currentPressedKey.objectName())
        self.lineEdit_KeyNumber.setText(str(self.currentPressedKey.keyNumber))
        self.lineEdit_KeyCode.setText(str(self.currentPressedKey.keyCode))

    def RemapKey(self):
        self.currentPressedKey.keyCode = self.lineEdit_KeyCode.text()
        self.currentPressedKey.setText(self.lineEdit_KeyCode.text())

    def RemapKey2(self):
        self.currentPressedKey.keyCode = KEY_BOARD_CODES_[self.comboBox_KeyName.currentText()]
        self.lineEdit_KeyCode.setText(str(self.currentPressedKey.keyCode))

        self.currentPressedKey.setText(self.comboBox_KeyName.currentText())
        print(self.currentPressedKey.keyCode)

        self.Map[self.currentPressedKey.keyNumber] = self.currentPressedKey.keyCode

    def SaveKeys(self):
        print(self.Map)
        self.SaveMap()

    def ReadMap(self):
        with open('../config/keyboard_map.txt', 'r') as file:
            map_str = file.read()
            self.Map = eval(map_str)
            print(self.Map)
            file.close()
        for bt_number,keyCode in self.Map.items():
            self.groupBox_Keyboard.children()[1 + bt_number].keyCode = keyCode
            self.groupBox_Keyboard.children()[1 + bt_number].setText(KEY_BOARD_CODES[keyCode])

    def SaveMap(self):
        with open('../config/keyboard_map.txt', 'w') as file:
            file.write(str(self.Map))
            file.close()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 设置其窗口尺寸显示正常
    __app = QApplication(sys.argv)
    # __app.setStyle('fusion')  # 设置 fusion 风格
    # __app.setStyle('windows')  # 设置 windows 风格
    __app.setStyle('windowsvista')  # 设置 windowsvista 风格
    myWin = Sub_Remap()
    myWin.show()
    sys.exit(__app.exec_())
