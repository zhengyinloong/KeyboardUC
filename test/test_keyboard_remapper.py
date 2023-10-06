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

from remapper import Ui_Form
from config.settings import *


class Sub_Remap(QWidget, Ui_Form):
    def __init__(self):
        super(Sub_Remap, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================
        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.currentPressedKey = None
        self.resize(UI_WIDTH, UI_HEIGHT)

        for btnumber in range(len(self.groupBox_Keyboard.children()[1:])):
            self.groupBox_Keyboard.children()[1+btnumber].keyNumber = btnumber
            self.groupBox_Keyboard.children()[1+btnumber].keyCode = None
            # self.groupBox_Keyboard.children()[1 + btnumber].setText('None')


    def CallBackFunctions(self):
        # key
        for bt in self.groupBox_Keyboard.children()[1:]:
            bt.clicked.connect(lambda _, button=bt: self.PressKey(button))
            bt.number = bt.objectName()
        # button
        self.pushButton_SetUp.clicked.connect(self.SetUpKeys)
        # lineEdit
        self.lineEdit_KeyCode.textChanged.connect(self.RemapKey)

    def PressKey(self, button):
        self.currentPressedKey = button
        print(self.currentPressedKey.objectName())
        self.lineEdit_KeyNumber.setText(str(self.currentPressedKey.keyNumber))
        self.lineEdit_KeyCode.setText(self.currentPressedKey.keyCode)

    def RemapKey(self):
        self.currentPressedKey.keyCode = self.lineEdit_KeyCode.text()
        self.currentPressedKey.setText(self.lineEdit_KeyCode.text())

    def SetUpKeys(self):
        pass


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 设置其窗口尺寸显示正常
    __app = QApplication(sys.argv)
    # __app.setStyle('fusion')  # 设置 fusion 风格
    # __app.setStyle('windows')  # 设置 windows 风格
    __app.setStyle('windowsvista')  # 设置 windowsvista 风格
    myWin = Sub_Remap()
    myWin.show()
    sys.exit(__app.exec_())
