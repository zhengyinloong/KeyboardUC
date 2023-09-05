# -*- coding:utf-8 -*-
# bushound.py in KeyboardUC
# zhengyinloong
# 2023/09/01 11:21

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class BusHoundSimulatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bus Hound Simulator")
        self.setGeometry(100, 100, 400, 200)

        self.capture_label = QLabel("Capture Data: Not Running", self)
        self.capture_label.setGeometry(20, 20, 300, 30)

        self.start_button = QPushButton("Start Capture", self)
        self.start_button.setGeometry(20, 60, 120, 30)
        self.start_button.clicked.connect(self.start_capture)

        self.stop_button = QPushButton("Stop Capture", self)
        self.stop_button.setGeometry(150, 60, 120, 30)
        self.stop_button.clicked.connect(self.stop_capture)
        self.stop_button.setEnabled(False)

        self.is_running = False

    def start_capture(self):
        self.is_running = True
        self.capture_label.setText("Capture Data: Running")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        # 在这里添加开始捕获数据的代码逻辑

    def stop_capture(self):
        self.is_running = False
        self.capture_label.setText("Capture Data: Not Running")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

        # 在这里添加停止捕获数据的代码逻辑


# 创建应用程序实例
app = QApplication(sys.argv)

# 创建窗口实例
window = BusHoundSimulatorGUI()
window.show()

# 执行应用程序主循环
sys.exit(app.exec_())
