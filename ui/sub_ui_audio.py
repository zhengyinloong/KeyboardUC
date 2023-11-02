# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_ui_audio.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Subui_Audio(object):
    def setupUi(self, Subui_Audio):
        Subui_Audio.setObjectName("Subui_Audio")
        Subui_Audio.resize(807, 494)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Subui_Audio)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_Input = QtWidgets.QGroupBox(Subui_Audio)
        self.groupBox_Input.setObjectName("groupBox_Input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_Input)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_MicrophoneTest = QtWidgets.QPushButton(self.groupBox_Input)
        self.pushButton_MicrophoneTest.setObjectName("pushButton_MicrophoneTest")
        self.verticalLayout.addWidget(self.pushButton_MicrophoneTest)
        self.horizontalLayout.addWidget(self.groupBox_Input)
        self.groupBox_Output = QtWidgets.QGroupBox(Subui_Audio)
        self.groupBox_Output.setObjectName("groupBox_Output")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Output)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_display = QtWidgets.QPushButton(self.groupBox_Output)
        self.pushButton_display.setObjectName("pushButton_display")
        self.gridLayout.addWidget(self.pushButton_display, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_Output)

        self.retranslateUi(Subui_Audio)
        QtCore.QMetaObject.connectSlotsByName(Subui_Audio)

    def retranslateUi(self, Subui_Audio):
        _translate = QtCore.QCoreApplication.translate
        Subui_Audio.setWindowTitle(_translate("Subui_Audio", "Audio"))
        self.groupBox_Input.setTitle(_translate("Subui_Audio", "Input"))
        self.pushButton_MicrophoneTest.setText(_translate("Subui_Audio", "test"))
        self.groupBox_Output.setTitle(_translate("Subui_Audio", "Output"))
        self.pushButton_display.setText(_translate("Subui_Audio", "demo display"))
