# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_USB = QtWidgets.QPushButton(self.centralwidget)
        self.btn_USB.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_USB.setObjectName("btn_USB")
        self.verticalLayout.addWidget(self.btn_USB)
        self.btn_BlueTooth = QtWidgets.QPushButton(self.centralwidget)
        self.btn_BlueTooth.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_BlueTooth.setObjectName("btn_BlueTooth")
        self.verticalLayout.addWidget(self.btn_BlueTooth)
        self.btn_KeyboardLayout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_KeyboardLayout.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_KeyboardLayout.setObjectName("btn_KeyboardLayout")
        self.verticalLayout.addWidget(self.btn_KeyboardLayout)
        self.btn_IAP = QtWidgets.QPushButton(self.centralwidget)
        self.btn_IAP.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_IAP.setObjectName("btn_IAP")
        self.verticalLayout.addWidget(self.btn_IAP)
        self.btn_Audio = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Audio.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_Audio.setObjectName("btn_Audio")
        self.verticalLayout.addWidget(self.btn_Audio)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 28))
        self.menubar.setObjectName("menubar")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuSystem.addAction(self.actionSettings)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSystem.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeyboardUC"))
        self.btn_USB.setText(_translate("MainWindow", "USB"))
        self.btn_BlueTooth.setText(_translate("MainWindow", "BlueTooth"))
        self.btn_KeyboardLayout.setText(_translate("MainWindow", "Keyboard Layout"))
        self.btn_IAP.setText(_translate("MainWindow", "IAP"))
        self.btn_Audio.setText(_translate("MainWindow", "Audio"))
        self.menuSystem.setTitle(_translate("MainWindow", "System"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About KeyboardUC"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionHelp.setText(_translate("MainWindow", "KeyboardUC help"))
