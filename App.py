import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.file_dialog().show()

    def file_dialog(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.ExistingFile)
