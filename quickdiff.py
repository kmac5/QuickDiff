import sys
import subprocess

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QMainWindow,
                             QLabel,
                             QLineEdit,
                             QApplication,
                             QPushButton)


class FileEdit(QLineEdit):
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)
        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            self.setText(filepath)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setMinimumSize(QtCore.QSize(620, 180))
        self.setWindowTitle("QuickDiff")

        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('File 1:')
        self.line1 = FileEdit(self)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('File 2:')
        self.line2 = FileEdit(self)

        self.line1.move(80, 20)
        self.line1.resize(502, 32)
        self.nameLabel1.move(20, 20)

        self.line2.move(80, 60)
        self.line2.resize(502, 32)
        self.nameLabel2.move(20, 60)

        pybutton = QPushButton('Swap Files', self)
        pybutton.clicked.connect(self.click_method_swap)
        pybutton.resize(162,32)
        pybutton.move(80, 100)

        pybutton = QPushButton('Toggle On Top', self)
        pybutton.clicked.connect(self.click_method_toggle)
        pybutton.resize(162,32)
        pybutton.move(250, 100)

        pybutton = QPushButton('Diff', self)
        pybutton.clicked.connect(self.click_method_diff)
        pybutton.resize(162,32)
        pybutton.move(420, 100)

    def click_method_swap(self):
        line1 = self.line1.text()
        line2 = self.line2.text()
        self.line1.setText(line2)
        self.line2.setText(line1)

    def click_method_toggle(self):
        on = bool(self.windowFlags() & QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, not on)
        self.show()

    def click_method_diff(self):
        line1 = self.line1.text()
        line2 = self.line2.text()
        subprocess.Popen(['gvim', '-d', line1, line2],
                creationflags=subprocess.CREATE_NEW_CONSOLE)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
