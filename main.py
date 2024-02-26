#!/home/hunanyan/python/piggame/.venv/bin/python
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QPushButton
import main_window

app = QApplication(sys.argv)
window = main_window.PigGameMainWindow()
window.show()
app.exec()

# TEST comment
