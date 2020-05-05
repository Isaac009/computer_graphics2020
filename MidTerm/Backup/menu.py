

import sys
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        lagrang = QtWidgets.QPushButton("Lagrang", self)
        lagrang.move(30, 50)

        bezier = QtWidgets.QPushButton("Bezier", self)
        bezier.move(150, 50)

        hermite = QtWidgets.QPushButton("Hermite", self)
        hermite.move(30, 110)

        cubic_spline = QtWidgets.QPushButton("Cubic Spline", self)
        cubic_spline.move(150, 110)

        close_button = QtWidgets.QPushButton("Close", self)
        close_button.move(90, 160)
      
        lagrang.clicked.connect(self.buttonClicked)            
        bezier.clicked.connect(self.buttonClicked)
        hermite.clicked.connect(self.buttonClicked)            
        cubic_spline.clicked.connect(self.buttonClicked)
        close_button.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 500, 290, 250)
        self.setWindowTitle('Application')
        self.show()
        
    def buttonClicked(self):
        from midterm_v2 import main_window
        sender = self.sender()
        if sender.text() == "Lagrang":
            self.close()
            print("Lagrang Selected.")
            main_window(mode_v=1)
        elif sender.text() == "Bezier":
            self.close()
            print("Bezier Selected.")
            self.close()
            main_window(mode_v=2)
        elif sender.text() == "Hermite":
            print("Hermite Selected.")
            self.close()
            main_window(mode_v=3)
        elif sender.text() == "Cubic Spline":
            print("Cubic Spline Selected.")
            self.close()
            main_window(mode_v=4)
        elif sender.text() == "Close":
            print("Close Selected.")
            self.close()
            main_window(mode_v=5)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Application Main Menu')

        layout = QtWidgets.QGridLayout()

        lagrang = QtWidgets.QPushButton("Lagrang", self)
        lagrang.move(30, 50)

        bezier = QtWidgets.QPushButton("Bezier", self)
        bezier.move(150, 50)

        hermite = QtWidgets.QPushButton("Hermite", self)
        hermite.move(30, 110)

        cubic_spline = QtWidgets.QPushButton("Cubic Spline", self)
        cubic_spline.move(150, 110)
      
        close_button = QtWidgets.QPushButton("Close", self)
        close_button.move(90, 160)
      
        lagrang.clicked.connect(self.buttonClicked)            
        bezier.clicked.connect(self.buttonClicked)
        hermite.clicked.connect(self.buttonClicked)            
        cubic_spline.clicked.connect(self.buttonClicked)
        close_button.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 500, 290, 250)
        self.setWindowTitle('Application')
        self.show()
        
    def buttonClicked(self):
        from midterm_v2 import main_window
        sender = self.sender()
        if sender.text() == "Lagrang":
            self.close()
            print("Lagrang Selected.")
            main_window(mode_v=1)
        elif sender.text() == "Bezier":
            self.close()
            print("Bezier Selected.")
            self.close()
            main_window(mode_v=2)
        elif sender.text() == "Hermite":
            print("Hermite Selected.")
            self.close()
            main_window(mode_v=3)
        elif sender.text() == "Cubic Spline":
            print("Cubic Spline Selected.")
            self.close()
            main_window(mode_v=4)
        elif sender.text() == "Close":
            print("Close Selected.")
            self.close()
            main_window(mode_v=5)

    def login(self):
        self.switch_window.emit()



class Controller:

    def __init__(self):
        self.login = Login()

        
    def show_login(self):
        self.login = Login()
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.login.close()
        self.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()