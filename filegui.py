from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)
from pathlib import Path


class FileWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def showDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        if fname[0]:
            return fname[0]
