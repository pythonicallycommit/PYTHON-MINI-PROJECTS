from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time
from PyQt5.uic import loadUiType

ui,_ = loadUiType('tabss.ui')


class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tab1to2)
        self.pushButton_3.clicked.connect(self.tab2to3)
        self.pushButton_2.clicked.connect(self.tab2to1)
        self.pushButton_4.clicked.connect(self.tab3to2)

    def tab1to2(self):
        self.tabWidget.setCurrentIndex(1)
    def tab2to1(self):
        self.tabWidget.setCurrentIndex(0)
    def tab2to3(self):
        self.tabWidget.setCurrentIndex(2)
    def tab3to2(self):
        self.tabWidget.setCurrentIndex(1)




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()