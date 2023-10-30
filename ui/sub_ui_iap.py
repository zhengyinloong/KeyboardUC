# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_ui_iap.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Subui_IAP(object):
    def setupUi(self, Subui_IAP):
        Subui_IAP.setObjectName("Subui_IAP")
        Subui_IAP.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Subui_IAP)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OpenFile.setGeometry(QtCore.QRect(690, 120, 89, 25))
        self.pushButton_OpenFile.setObjectName("pushButton_OpenFile")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 651, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 180, 521, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(580, 180, 201, 341))
        self.textBrowser_2.setObjectName("textBrowser_2")
        Subui_IAP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Subui_IAP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        self.menuSettings = QtWidgets.QMenu(self.menuSystem)
        self.menuSettings.setObjectName("menuSettings")
        Subui_IAP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Subui_IAP)
        self.statusbar.setObjectName("statusbar")
        Subui_IAP.setStatusBar(self.statusbar)
        self.actionFonts = QtWidgets.QAction(Subui_IAP)
        self.actionFonts.setObjectName("actionFonts")
        self.actionQuit = QtWidgets.QAction(Subui_IAP)
        self.actionQuit.setObjectName("actionQuit")
        self.menuSettings.addAction(self.actionFonts)
        self.menuSystem.addAction(self.menuSettings.menuAction())
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionQuit)
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(Subui_IAP)
        QtCore.QMetaObject.connectSlotsByName(Subui_IAP)

    def retranslateUi(self, Subui_IAP):
        _translate = QtCore.QCoreApplication.translate
        Subui_IAP.setWindowTitle(_translate("Subui_IAP", "IAP"))
        self.pushButton_OpenFile.setText(_translate("Subui_IAP", "Open file"))
        self.menuSystem.setTitle(_translate("Subui_IAP", "System"))
        self.menuSettings.setTitle(_translate("Subui_IAP", "Settings"))
        self.actionFonts.setText(_translate("Subui_IAP", "Fonts"))
        self.actionQuit.setText(_translate("Subui_IAP", "Quit"))
