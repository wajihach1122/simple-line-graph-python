# -*- coding: utf-8 -*-
"""
Created on Tue May  6 16:59:17 2025

@author: test
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('hello world')
window.setGeometry(100, 100, 280, 80)

label = QLabel ('hello first app', parent=window)
window.show()
sys.exit(app.exec_())