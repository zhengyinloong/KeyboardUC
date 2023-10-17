# -*- coding:utf-8 -*-
# main.py in KeyboardUC
# zhengyinloong
# 2023/08/30 02:38

import bluetooth
import usb
from ui.main_ui import *
from ui.sub_ui_usb import *
from ui.sub_ui_bluetooth import *
from ui.sub_ui_iap import *
from ui.sub_ui_keyboard_layout import *
from config.settings import *
from user import usbdriver, bluetoothdriver
import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFontDialog, QFileDialog, QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtCore

import subprocess

command = 'sudo -S chmod 777 */ -R'
password = PASSWORD
process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
process.communicate(password.encode())


# sudo chmod 777 */ -R
# sudo -S python3 main.py
class Worker(QObject):
    finished = pyqtSignal()
    received_data = pyqtSignal(str)

    def __init__(self, Device, ep_in):
        super().__init__()
        self.Device = Device
        self.ep_in = ep_in
        self.isRecv = False

    def ReceiveData(self):
        while self.isRecv:
            try:
                data_recv = usbdriver.ReceiveData(self.Device, self.ep_in)
                if data_recv is not None:
                    parsed_data = self.ParsingData(data_recv)
                    output = ''
                    for t, d in parsed_data.items():
                        output += f'{t}:{d}\n'

                    self.received_data.emit(f'{output}')
            except Exception as e:
                # print(e)
                self.received_data.emit(f'{e}')
                continue
                # break
        self.finished.emit()

    def ParsingData(self, data):
        """
        鼠标发送给PC的数据每次4个字节
            BYTE1 BYTE2 BYTE3 BYTE4
            定义分别是：
            BYTE1 --
                   |--bit7:   1   表示   Y   坐标的变化量超出－256   ~   255的范围,0表示没有溢出
                   |--bit6:   1   表示   X   坐标的变化量超出－256   ~   255的范围，0表示没有溢出
                   |--bit5:   Y   坐标变化的符号位，1表示负数，即鼠标向下移动
                   |--bit4:   X   坐标变化的符号位，1表示负数，即鼠标向左移动
                   |--bit3:     恒为1
                   |--bit2:     1表示中键按下
                   |--bit1:     1表示右键按下
                   |--bit0:     1表示左键按下
            BYTE2 -- X坐标变化量，与byte的bit4组成9位符号数,负数表示向左移，正数表右移。用补码表示变化量
            BYTE3 -- Y坐标变化量，与byte的bit5组成9位符号数，负数表示向下移，正数表上移。用补码表示变化量
            BYTE4 -- 滚轮变化。
        键盘发送给PC的数据每次8个字节
            BYTE1 BYTE2 BYTE3 BYTE4 BYTE5 BYTE6 BYTE7 BYTE8
            定义分别是：

            BYTE0 --（0 = OFF，1 = ON，CONSTANT为保留位）
                   |--bit0:   NUM LOCK
                   |--bit1:   CAPS LOCK
                   |--bit2:   SCROLL LOCK
                   |--bit3:   COMPOSE
                   |--bit4:   KANA
                   |--bit5:   CONSTANT
                   |--bit6:   CONSTANT
                   |--bit7:   CONSTANT
            BYTE1 --
                   |--bit0:   Left Control是否按下，按下为1
                   |--bit1:   Left Shift  是否按下，按下为1
                   |--bit2:   Left Alt    是否按下，按下为1
                   |--bit3:   Left GUI    是否按下，按下为1
                   |--bit4:   Right Control是否按下，按下为1
                   |--bit5:   Right Shift 是否按下，按下为1
                   |--bit6:   Right Alt   是否按下，按下为1
                   |--bit7:   Right GUI   是否按下，按下为1
            BYTE2 -- 保留位
            BYTE3--BYTE8 -- 这六个为普通按键
        """
        byte1 = data[0]
        byte2 = data[1]
        byte3 = data[2]
        byte4 = data[3]

        x_overflow = (byte1 & 0b10000000) >> 7
        y_overflow = (byte1 & 0b01000000) >> 6
        y_negative = (byte1 & 0b00100000) >> 5
        x_negative = (byte1 & 0b00010000) >> 4
        middle_btn_pressed = (byte1 & 0b00000100) >> 2
        right_btn_pressed = (byte1 & 0b00000010) >> 1
        left_btn_pressed = byte1 & 0b00000001

        # Calculate X coordinate change
        x_change = byte2 if not x_negative else -(256 - byte2)

        # Calculate Y coordinate change
        y_change = byte3 if not y_negative else -(256 - byte3)

        # Get scroll wheel change
        scroll_change = byte4

        return {
            'x_overflow': bool(x_overflow),
            'y_overflow': bool(y_overflow),
            'x_negative': bool(x_negative),
            'y_negative': bool(y_negative),
            'middle_btn_pressed': bool(middle_btn_pressed),
            'right_btn_pressed': bool(right_btn_pressed),
            'left_btn_pressed': bool(left_btn_pressed),
            'x_change': x_change,
            'y_change': y_change,
            'scroll_change': scroll_change
        }


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================
        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.subwins = {'USB': Sub_USB(self),
                        'BlueTooth': Sub_BlueTooth(self),
                        'Keyboard Layout': Sub_KeyboardLayout(self),
                        'IAP': Sub_IAP(self)}

        self.resize(UI_WIDTH, UI_HEIGHT)

    def CallBackFunctions(self):
        # Menu bar
        self.actionQuit.triggered.connect(self.Quit)
        # self.actionSettings.triggered.connect(self.Quit)
        self.actionHelp.triggered.connect(self.Quit)
        self.actionAbout.triggered.connect(self.ShowAbout)

        # Buttons

        self.btn_USB.clicked.connect(lambda: self.OpenSubWindow('USB'))
        self.btn_BlueTooth.clicked.connect(lambda: self.OpenSubWindow('BlueTooth'))
        self.btn_KeyboardLayout.clicked.connect(lambda: self.OpenSubWindow('Keyboard Layout'))
        self.btn_IAP.clicked.connect(lambda: self.OpenSubWindow('IAP'))

    def OpenSubWindow(self, sub: str):
        self.subwins[sub].show()
        self.hide()

    def ShowAbout(self):
        about_text = """
        <html>
            <head>
                <style>
                    p { color:#FF23CC; }
                    body{font-family: "方正喵呜"; }
                </style>
            </head>
            <body>
                <h2>Keyboard UC v1.0</h2>
                <p>Production: Room 306,Experimental Building,NCEPU(Baoding)</p>
                <p>Author: Zheng Yinlong,NCEPU(Baoding)</p>
                <p>To learn more, please visit <a href="https://github.com/zhengyinloong/KeyboardUC">https://github.com/zhengyinloong</a></p>
            </body>
        </html>
        """

        QMessageBox.about(self, "About", about_text)

    def Quit(self):
        # ============ ADD ===========

        # QCoreApplication.quit()
        QCoreApplication.exit(0)


class Sub_USB(QMainWindow, Ui_Subui_USB):
    def __init__(self, parent):
        self.parent = parent
        super(Sub_USB, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================

        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.resize(UI_WIDTH, UI_HEIGHT)

        self.PrepParameters()
        self.PrepWidgets()

    def PrepParameters(self):

        self.worker = None
        self.thread = None

        self.Font = QFont()
        self.Font.setPixelSize(10)

        # self.VID = 0x0D00
        # self.PID = 0x0721
        # self.VID = 0x258A
        # self.PID = 0x0017
        self.VID = VENDOR_ID
        self.PID = PRODUCT_ID
        self.Interface_Number = 0x00
        self.Alternate_setting = 0x00

        self.Device = None

        self.data_send = '\x02\xff\x02'
        self.data_recv = None
        self.isRecv = False

    def PrepWidgets(self):

        self.lineEdit_VID.setText(str(self.VID))
        self.lineEdit_PID.setText(str(self.PID))
        self.lineEdit_Interface.setText(str(self.Interface_Number))

        self.textBrowser_RECEIVE.setFont(self.Font)
        self.textBrowser_SEND.setFont(self.Font)

    def CallBackFunctions(self):

        # Menu bar
        self.actionFonts.triggered.connect(lambda: self.SetFonts([
            self.textBrowser_RECEIVE,
            self.textBrowser_SEND]))
        self.actionQuit.triggered.connect(self.Quit)
        # Buttons
        self.pushButton_FindDevices.clicked.connect(self.FindDevices)
        self.pushButton_ConnectDevice.clicked.connect(self.ConnectDevice)
        self.pushButton_ReadConfig.clicked.connect(self.ReadConfig)
        self.pushButton_SendData.clicked.connect(self.SendData)
        # self.pushButton_ReceiveData.clicked.connect(self.ReceiveData)
        self.pushButton_ReceiveData.clicked.connect(self.onReceiveDataClicked)
        # self.pushButton_Stop.clicked.connect(self.ReceiveData)

        self.pushButton_Clear.clicked.connect(self.ClearHistory)

        # Changes
        self.lineEdit_VID.textChanged.connect(self.ParametersReload)
        self.lineEdit_PID.textChanged.connect(self.ParametersReload)
        self.lineEdit_Interface.textChanged.connect(self.ParametersReload)

    # ====================================================

    def onReceiveDataClicked(self):
        if not self.worker:
            self.worker = Worker(self.Device, self.ep_in)
            self.worker.received_data.connect(self.updateTextBrowser)
            self.worker.finished.connect(self.onWorkerFinished)

            self.thread = QThread()
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.ReceiveData)
            self.thread.start()

        self.worker.isRecv = not self.worker.isRecv
        self.pushButton_ReceiveData.setText('Stop' if self.worker.isRecv else 'Receive data')
        self.textBrowser_RECEIVE.append('Receive data' if self.worker.isRecv else 'Stop')

    def onWorkerFinished(self):
        self.worker = None
        self.thread.quit()
        self.thread.wait()
        self.thread = None

    @QtCore.pyqtSlot(str)
    def updateTextBrowser(self, text):
        self.textBrowser_RECEIVE.append(text)

    # ======================================================

    def SendData(self):
        try:
            usbdriver.SendData(self.Device, self.ep_out, self.data_send)
            self.textBrowser_SEND.append(f'{self.data_send}')
        except Exception as e:
            # print(e)
            self.textBrowser_SEND.append(f'{e}')

    # def ReceiveData(self):
    #     # self.isRecv = ~ self.isRecv
    #     self.isRecv ^= True
    #     self.pushButton_ReceiveData.setText('Stop' if self.isRecv else 'Receive data')
    #
    #     while self.isRecv:
    #         try:
    #             self.data_recv = usbdriver.ReceiveData(self.Device, self.ep_in)
    #             self.textBrowser_RECEIVE.append(f'{self.data_recv}')
    #         except Exception as e:
    #             print(e)
    #             self.textBrowser_RECEIVE.append(f'{e}')
    #             break
    #             # continue

    def ClearHistory(self):

        self.textBrowser_RECEIVE.clear()
        self.textBrowser_SEND.clear()

    def ParametersReload(self):
        try:
            self.VID = self.transe2int(self.lineEdit_VID.text())
            self.PID = self.transe2int(self.lineEdit_PID.text())
            self.Interface_Number = self.transe2int(self.lineEdit_Interface.text())
            # self.VID = int(self.lineEdit_VID.text())
        except:
            pass

    @staticmethod
    def transe2int(num_str: str):
        if ('x' in num_str) or ('X' in num_str):
            num = int(num_str, 16)
        else:
            num = int(num_str)
        return num

    def SetFonts(self, widgets):
        font, ok = QFontDialog.getFont()
        if ok:
            # for widget_ in widget.findChildren():
            self.Font = font
        if widgets:
            for widget in widgets:
                widget.setFont(self.Font)

    def FindDevices(self):
        try:
            devs = usbdriver.FindDevices()
            if devs:
                count = 0
                for device in usbdriver.FindDevices():
                    count += 1
                self.textBrowser_RECEIVE.append(f"FIND {count} DEVICES")
                for dev in usbdriver.FindDevices():
                    try:
                        dev_id = f'{dev.idVendor:04X}:{dev.idProduct:04X}'
                        dev_class = dev.bDeviceClass
                        dev_name = None
                        dev_usb = f'USB{int(hex(dev.bcdUSB)[2:]) / 100}'
                        try:
                            dev_name = f'{usb.util.get_string(dev, 2)}' if dev.iProduct == 2 else 'unknown'
                        except:
                            dev_name = f'unknown'
                        self.textBrowser_RECEIVE.append(f"ID: {dev_id} Name: {dev_name} {dev_usb}")
                    except:
                        pass
        except Exception as e:
            self.textBrowser_RECEIVE.append(f"NOT FOUND")
            self.textBrowser_RECEIVE.append(f"Error:{e}")

    def ConnectDevice(self):
        self.lastDevice = self.Device
        try:
            self.Device = usbdriver.FindDevice(self.VID, self.PID)
            if self.Device is None:

                self.textBrowser_RECEIVE.append(f'({self.VID}.{self.PID}) NOT FOUND')
                self.Device = self.lastDevice
            else:
                self.DeviceName = usb.util.get_string(self.Device, 2)  # 假设字符串描述符索引为 4
                self.textBrowser_RECEIVE.append(f'FIND ({self.VID}.{self.PID}):\n{self.DeviceName}')
        except Exception as e:
            self.Device = self.lastDevice
            self.textBrowser_RECEIVE.append(f'({self.VID}.{self.PID}) NOT FOUND')
            self.textBrowser_RECEIVE.append(f'Error:{e}')

    def ReadConfig(self):
        try:
            # self.config, self.interface = ReadConfig(
            #     self.Device, self.Interface_Number, self.Alternate_setting)
            #
            self.config, self.interface = usbdriver.ReadConfig(self.Device, self.Interface_Number)
            self.lineEdit_Interface.setText(f'{self.interface.bInterfaceNumber}')

            # self.textBrowser_RECEIVE.append(f'{self.Device}')

            self.ep_in, self.ep_out = usbdriver.Endpoints(self.interface)

            self.ParsingEndpoints()
            self.textBrowser_RECEIVE.append(f'endpoint in:\n{self.ep_in}')
            self.textBrowser_RECEIVE.append(f'endpoint out:\n{self.ep_out}')

        except Exception as e:
            self.textBrowser_RECEIVE.append(f'Error:{e}')

    def ParsingEndpoints(self):
        # 0 表示 控制端点，1 表示 Isochronous 端点，2 表示 Bulk 端点，3 表示 Interrupt 端点。
        class_dict = {0: 'Control',
                      1: 'Isochronous',
                      2: 'Bulk',
                      3: 'Interrupt'}

        if self.ep_in is not None:
            self.EPIAddress = self.ep_in.bEndpointAddress
            self.EPIClass = class_dict[self.ep_in.bmAttributes]
            self.EPILength = self.ep_in.bLength

            self.lineEdit_EPIAddress.setText(f'0x{self.EPIAddress:0X}')
            self.lineEdit_EPIClass.setText(f'{self.EPIClass}')
            self.lineEdit_EPILength.setText(f'{self.EPILength}')
        if self.ep_out is not None:
            self.EPOAddress = self.ep_out.bEndpointAddress
            self.EPOClass = class_dict[self.ep_out.bmAttributes]
            self.EPOLength = self.ep_out.bLength

            self.lineEdit_EPOAddress.setText(f'0x{self.EPOAddress:0X}')
            self.lineEdit_EPOClass.setText(f'{self.EPOClass}')
            self.lineEdit_EPOLength.setText(f'{self.EPOLength}')

    def ReleaseDevice(self):
        if self.Device is not None:
            try:
                usbdriver.ReleaseDevice(self.Device, self.Interface_Number)
            except Exception as e:
                print(f'{e}')

    def Quit(self):
        self.close()
        # QCoreApplication.quit()
        # QCoreApplication.exit(0)

    def DoIfQuit(self):
        # ============ ADD ===========
        self.ReleaseDevice()
        self.parent.show()
        print(f'quit{self}')

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            self.DoIfQuit()
            event.accept()
        else:
            event.ignore()


class Sub_BlueTooth(QMainWindow, Ui_Subui_BlueTooth):
    def __init__(self, parent):
        self.parent = parent
        super(Sub_BlueTooth, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================

        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.resize(UI_WIDTH, UI_HEIGHT)

        self.PrepParameters()
        self.PrepWidgets()

    def PrepParameters(self):
        self.Device = None
        self.Address = '14:DD:9C:BC:51:7C'

    def PrepWidgets(self):
        self.lineEdit_Address.setText(str(self.Address))
        pass

    def CallBackFunctions(self):
        self.actionFonts.triggered.connect(lambda: self.SetFonts([self.textBrowser_RECEIVE,
                                                                  self.textBrowser_SEND]))
        self.actionQuit.triggered.connect(self.Quit)

        self.pushButton_FindDevices.clicked.connect(self.FindDevices)
        self.pushButton_ConnectDevice.clicked.connect(self.ConnectDevice)
        self.lineEdit_Address.textChanged.connect(self.ParametersReload)

        self.pushButton_Clear.clicked.connect(self.ClearHistory)

        pass

    def SendData(self):
        pass

    def ReceiveData(self):
        pass

    def ClearHistory(self):

        self.textBrowser_RECEIVE.clear()
        self.textBrowser_SEND.clear()
        pass

    def ParametersReload(self):
        self.Address = self.lineEdit_Address.text()
        pass

    @staticmethod
    def transe2int(num_str: str):
        if ('x' in num_str) or ('X' in num_str):
            num = int(num_str, 16)
        else:
            num = int(num_str)
        return num

    def SetFonts(self, widgets):
        font, ok = QFontDialog.getFont()
        if ok:
            # for widget_ in widget.findChildren():
            self.Font = font
        if widgets:
            for widget in widgets:
                widget.setFont(self.Font)

    def FindDevices(self):
        self.textBrowser_RECEIVE.append(f"Searching for devices, please wait ...")
        try:
            devs = bluetoothdriver.FindDevices()
            if devs:
                count = 0
                for device in devs:
                    count += 1
                self.textBrowser_RECEIVE.append(f"FIND {count} DEVICES")
                for dev in iter(devs):
                    name = bluetooth.lookup_name(dev)
                    self.textBrowser_RECEIVE.append(f"{dev} : {name}")
        except Exception as e:
            self.textBrowser_RECEIVE.append(f"NOT FOUND")
            self.textBrowser_RECEIVE.append(f"Error:{e}")

    def ConnectDevice(self):
        self.lastDevice = self.Device
        try:
            self.Device = bluetoothdriver.ConnectDevice(self.Address)
            if self.Device is None:
                self.textBrowser_RECEIVE.append(f'({self.Address}) NOT FOUND')
                self.Device = self.lastDevice
            else:
                self.DeviceName = name = bluetooth.lookup_name(self.Device)
                self.textBrowser_RECEIVE.append(f'FIND ({self.Address}):\n{self.DeviceName}')
        except Exception as e:
            self.Device = self.lastDevice
            self.textBrowser_RECEIVE.append(f'({self.Address}) NOT FOUND')
            self.textBrowser_RECEIVE.append(f'Error:{e}')

        pass

    def ReadConfig(self):
        pass

    def Quit(self):
        self.close()
        # QCoreApplication.quit()
        # QCoreApplication.exit(0)

    def DoIfQuit(self):
        # ============ ADD ===========
        # self.ReleaseDevice()
        self.parent.show()
        print(f'quit{self}')

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            self.DoIfQuit()
            event.accept()
        else:
            event.ignore()


class Sub_IAP(QMainWindow, Ui_Subui_IAP):
    def __init__(self, parent):
        self.parent = parent
        super(Sub_IAP, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================

        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.resize(UI_WIDTH, UI_HEIGHT)

        self.PrepParameters()
        self.PrepWidgets()

    def PrepParameters(self):
        pass

    def PrepWidgets(self):

        pass

    def CallBackFunctions(self):
        self.actionFonts.triggered.connect(lambda: self.SetFonts([]))

        self.actionQuit.triggered.connect(self.Quit)
        self.pushButton_OpenFile.clicked.connect(self.OpenFile)

    def OpenFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Load File', '', 'All Files (*)', options=options)

        if '.bin' in file_name:
            # print(file_name)
            self.file_name = file_name
            self.lineEdit.setText(f'{self.file_name}')
            self.textBrowser_2.append(f'{self.file_name}Load bin successfully')

            self.DownloadFile()
        else:
            self.textBrowser_2.append(f'{file_name} is not a bin file,please reload.')

    def DownloadFile(self):

        with open(self.file_name, 'rb') as file:
            content = file.read()
            print(content)
            self.textBrowser.append(f'{content}')
            # 对文件内容进行处理，可以在这里编写你的逻辑

    def ReceiveData(self):
        pass

    def ClearHistory(self):

        # self.textBrowser_RECEIVE.clear()
        # self.textBrowser_SEND.clear()
        pass

    def ParametersReload(self):
        pass

    @staticmethod
    def transe2int(num_str: str):
        if ('x' in num_str) or ('X' in num_str):
            num = int(num_str, 16)
        else:
            num = int(num_str)
        return num

    def SetFonts(self, widgets):
        font, ok = QFontDialog.getFont()
        if ok:
            # for widget_ in widget.findChildren():
            self.Font = font
        if widgets:
            for widget in widgets:
                widget.setFont(self.Font)

    def FindDevices(self):
        pass

    def ConnectDevice(self):
        pass

    def ReadConfig(self):
        pass

    def Quit(self):
        self.close()
        # QCoreApplication.quit()
        # QCoreApplication.exit(0)

    def DoIfQuit(self):
        # ============ ADD ===========
        # self.ReleaseDevice()
        self.parent.show()
        print(f'quit{self}')

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            self.DoIfQuit()
            event.accept()
        else:
            event.ignore()


class Sub_KeyboardLayout(QWidget, Ui_Subui_KeyboardLayout):
    def __init__(self, parent):
        self.parent = parent
        super(Sub_KeyboardLayout, self).__init__()
        self.setupUi(self)
        # ============ ADD ====================

        self.PrepOpen()  # 初始化参数和控件状态
        self.CallBackFunctions()  # 各个控件的功能函数集

    def PrepOpen(self):
        self.resize(UI_WIDTH, UI_HEIGHT)

        self.PrepParameters()
        self.PrepWidgets()

    def PrepParameters(self):

        pass

    def PrepWidgets(self):

        # buttons init
        for bt_number in range(len(self.groupBox_Keyboard.children()[1:])):
            self.groupBox_Keyboard.children()[1 + bt_number].keyNumber = bt_number
            self.groupBox_Keyboard.children()[1 + bt_number].keyCode = None
            # self.groupBox_Keyboard.children()[1 + bt_number].setText('None')
        # keyboard_map
        self.Map = {}
        self.ReadMap()

        self.currentPressedKey = self.pushButton_1
        self.currentPressedKey.setStyleSheet('QPushButton{background:#42cdea;}')
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
        self.currentPressedKey.setStyleSheet('QPushButton{background:#42cdea;}')
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
        # print(self.Map)
        self.SaveMap()

    def ReadMap(self):
        with open('./config/keyboard_map.txt', 'r') as file:
            map_str = file.read()
            self.Map = eval(map_str)
            # print(self.Map)
            file.close()
        for bt_number, keyCode in self.Map.items():
            self.groupBox_Keyboard.children()[1 + bt_number].keyCode = keyCode
            self.groupBox_Keyboard.children()[1 + bt_number].setText(KEY_BOARD_CODES[keyCode])

    def SaveMap(self):
        with open('./config/keyboard_map.txt', 'w') as file:
            file.write(str(self.Map))
            file.close()

    def Quit(self):
        self.close()
        # QCoreApplication.quit()
        # QCoreApplication.exit(0)

    def DoIfQuit(self):
        # ============ ADD ===========
        self.parent.show()
        print(f'quit{self}')

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            self.DoIfQuit()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 设置其窗口尺寸显示正常
    __app = QApplication(sys.argv)
    # __app.setStyle('fusion')  # 设置 fusion 风格
    # __app.setStyle('windows')  # 设置 windows 风格
    __app.setStyle('windowsvista')  # 设置 windowsvista 风格
    myWin = Main()
    myWin.show()
    sys.exit(__app.exec_())
