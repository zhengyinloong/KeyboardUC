# -*- coding:utf-8 -*-
# main.py in KeyboardUC
# zhengyinloong
# 2023/08/30 02:38
import bluetooth
import usb
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFontDialog, QFileDialog
from ui.main_ui import *
from ui.sub_ui_usb import *
from ui.sub_ui_bluetooth import *
from ui.sub_ui_iap import *
from config.settings import *
from user import usbdriver, bluetoothdriver
import sys

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
                self.received_data.emit(f'{data_recv}')
            except Exception as e:
                print(e)
                self.received_data.emit(f'{e}')
                continue
                # break
        self.finished.emit()


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
    def __init__(self, parentwin):
        self.parentwin = parentwin
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
        self.VID = 0x25A7
        self.PID = 0xFA23
        self.Interface_Number = 0x0
        self.Alternate_setting = 0x0

        self.Device = None

        self.data_send = None
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
            # SendData(self.Device, self.ep_out, self.data_send)
            self.textBrowser_SEND.append(f'{self.data_send}')
        except Exception as e:
            print(e)
            self.textBrowser_SEND.append(f'{e}')

    def ReceiveData(self):
        # self.isRecv = ~ self.isRecv
        self.isRecv ^= True
        self.pushButton_ReceiveData.setText('Stop' if self.isRecv else 'Receive data')

        while self.isRecv:
            try:
                self.data_recv = usbdriver.ReceiveData(self.Device, self.ep_in)
                self.textBrowser_RECEIVE.append(f'{self.data_recv}')
            except Exception as e:
                print(e)
                self.textBrowser_RECEIVE.append(f'{e}')
                break
                # continue

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
                for dev in devs:
                    self.textBrowser_RECEIVE.append(f"{dev}")
        except Exception as e:
            self.textBrowser_RECEIVE.append(f"NOT FOUND:\n{e}")

    def ConnectDevice(self):
        self.lastDevice = self.Device
        try:
            self.Device = usbdriver.FindDevice(self.VID, self.PID)
            if self.Device == None:

                self.textBrowser_RECEIVE.append(f'({self.VID}.{self.PID}) NOT FOUND')
                self.Device = self.lastDevice
            else:
                self.DeviceName = usb.util.get_string(self.Device, 2)  # 假设字符串描述符索引为 4
                self.textBrowser_RECEIVE.append(f'FIND ({self.VID}.{self.PID}):\n{self.DeviceName}')
        except Exception as e:
            self.Device = self.lastDevice
            self.textBrowser_RECEIVE.append(f'({self.VID}.{self.PID}) NOT FOUND')
            self.textBrowser_RECEIVE.append(f'{e}')

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
            self.textBrowser_RECEIVE.append(f'{e}')

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

    def Quit(self):
        self.close()
        # QCoreApplication.quit()
        # QCoreApplication.exit(0)
        # ============ ADD ===========

        self.parentwin.show()

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            # print("执行关闭操作")
            self.Quit()
            event.accept()
        else:
            event.ignore()


class Sub_BlueTooth(QMainWindow, Ui_Subui_BlueTooth):
    def __init__(self, parentwin):
        self.parentwin = parentwin
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
        pass

    def PrepWidgets(self):

        pass

    def CallBackFunctions(self):
        self.actionFonts.triggered.connect(lambda: self.SetFonts([self.textBrowser_RECEIVE,
                                                                  self.textBrowser_SEND]))
        self.actionQuit.triggered.connect(self.Quit)

        self.pushButton_FindDevices.clicked.connect(self.FindDevices)
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
            self.textBrowser_RECEIVE.append(f"NOT FOUND:\n{e}")

    def ConnectDevice(self):
        self.lastDevice = self.Device
        pass

    def ReadConfig(self):
        pass

    def Quit(self):
        self.close()
        # QCoreApplication.quit()
        # QCoreApplication.exit(0)
        # ============ ADD ===========

        self.parentwin.show()

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            # print("执行关闭操作")
            self.Quit()
            event.accept()
        else:
            event.ignore()


class Sub_IAP(QMainWindow, Ui_Subui_IAP):
    def __init__(self, parentwin):
        self.parentwin = parentwin
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
        self.pushButton.clicked.connect(self.LoadFile)

    def LoadFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Load File', '', 'All Files (*)', options=options)
        print(file_name)
        if '.bin' in file_name:
            print('Load bin sucessfully')
            self.file_name = file_name
            self.DownloadFile()

    def DownloadFile(self):

        with open(self.file_name, 'rb') as file:
            content = file.read()
            print(content)
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
        # ============ ADD ===========

        self.parentwin.show()

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, '确认', '确定要关闭窗口吗？', QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        reply = QMessageBox.Yes
        if reply == QMessageBox.Yes:
            # 执行你自定义的操作，比如保存数据或清理资源
            # print("执行关闭操作")
            self.Quit()
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
