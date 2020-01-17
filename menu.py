import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import Main


a = []
openWin = False  # Проверка, открыто ли окно


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.pb1.clicked.connect(self.start)
        self.pb3.clicked.connect(self.quit)

    def start(self):
        self.pb1.setEnabled(False)
        Main.startGame()




    def quit(self):
        quit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
