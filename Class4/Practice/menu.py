

import sys
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        btn_lagrang = QtWidgets.QPushButton("Lagrang", self)
        btn_lagrang.move(30, 50)

        btn_bezier = QtWidgets.QPushButton("Bezier", self)
        btn_bezier.move(150, 50)

        btn3 = QtWidgets.QPushButton("Hermite", self)
        btn3.move(30, 110)

        btn4 = QtWidgets.QPushButton("Cubic Spline", self)
        btn4.move(150, 110)

        btn5 = QtWidgets.QPushButton("Close", self)
        btn5.move(150, 160)
      
        btn_lagrang.clicked.connect(self.buttonClicked)            
        btn_bezier.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)            
        btn4.clicked.connect(self.buttonClicked)
        btn5.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('Application')
        self.show()
        
    def buttonClicked(self):
        from midterm_v2 import main_window
        sender = self.sender()
        if sender.text() == "Lagrang":
            self.close()
            print("Lagrang clicked.")
            main_window(mode_v=1)
        elif sender.text() == "Bezier":
            self.close()
            print("Bezier clicked.")
            self.close()
            main_window(mode_v=2)
        elif sender.text() == "Hermite":
            print("Hermite clicked.")
            self.close()
            main_window(mode_v=3)
        elif sender.text() == "Cubic Spline":
            print("Cubic Spline clicked.")
            self.close()
            main_window(mode_v=4)
        elif sender.text() == "Close":
            print("Close clicked.")
            self.close()
            main_window(mode_v=5)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


# class WindowTwo(QtWidgets.QWidget):

#     def __init__(self, text):
#         QtWidgets.QWidget.__init__(self)
#         self.setWindowTitle('Window Two')

#         layout = QtWidgets.QGridLayout()

#         self.label = QtWidgets.QLabel(text)
#         layout.addWidget(self.label)

#         self.button = QtWidgets.QPushButton('Close')
#         self.button.clicked.connect(self.close)

#         layout.addWidget(self.button)

#         self.setLayout(layout)


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Application Main Menu')

        layout = QtWidgets.QGridLayout()

        btn_lagrang = QtWidgets.QPushButton("Lagrang", self)
        btn_lagrang.move(30, 50)

        btn_bezier = QtWidgets.QPushButton("Bezier", self)
        btn_bezier.move(150, 50)

        btn3 = QtWidgets.QPushButton("Hermite", self)
        btn3.move(30, 110)

        btn4 = QtWidgets.QPushButton("Cubic Spline", self)
        btn4.move(150, 110)
      
        btn5 = QtWidgets.QPushButton("Close", self)
        btn5.move(150, 160)
      
        btn_lagrang.clicked.connect(self.buttonClicked)            
        btn_bezier.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)            
        btn4.clicked.connect(self.buttonClicked)
        btn5.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('Application Main Menu')
        self.show()
        
    def buttonClicked(self):
        from midterm_v2 import main_window
        sender = self.sender()
        if sender.text() == "Lagrang":
            print("Lagrang Selected.")
            main_window(mode_v=1)
        elif sender.text() == "Bezier":
            print("Bezier Selected.")
            main_window(mode_v=2)
        elif sender.text() == "Hermite":
            print("Hermite Selected.")
            main_window(mode_v=3)
        elif sender.text() == "Cubic Spline":
            print("Cubic Spline Selected.")
            main_window(mode_v=4)
        elif sender.text() == "Close":
            print("Close clicked.")
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