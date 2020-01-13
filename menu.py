import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import sqlite3
import Main


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.pb1.clicked.connect(self.start)
        self.pb2.clicked.connect(self.table)
        self.pb3.clicked.connect(self.quit)
        self.con = sqlite3.connect('table.db')
        self.cur = self.con.cursor()

    def start(self):
        Main.main()

    def table(self):
        pass

    def quit(self):
        quit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
