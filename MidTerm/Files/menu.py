import sys
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        btn_lagrange = QtWidgets.QPushButton("Lagrange", self)
        btn_lagrange.move(30, 50)

        btn_bezier = QtWidgets.QPushButton("Bezier", self)
        btn_bezier.move(150, 50)

        btn_hermite = QtWidgets.QPushButton("Hermite", self)
        btn_hermite.move(30, 110)

        btn_cubic_spline = QtWidgets.QPushButton("Cubic Spline", self)
        btn_cubic_spline.move(150, 110)

        btn_close = QtWidgets.QPushButton("Close", self)
        btn_close.move(150, 160)
      
        btn_lagrange.clicked.connect(self.buttonClicked)            
        btn_bezier.clicked.connect(self.buttonClicked)
        btn_hermite.clicked.connect(self.buttonClicked)            
        btn_cubic_spline.clicked.connect(self.buttonClicked)
        btn_close.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('Application')
        self.show()
        
    def buttonClicked(self):
        from midterm_v2 import main_window
        sender = self.sender()
        if sender.text() == "Lagrange":
            self.close()
            print("Lagrange clicked.")
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

class MenuClass(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Application Main Menu')

        layout = QtWidgets.QGridLayout()

        btn_lagrange = QtWidgets.QPushButton("Lagrange", self)
        btn_lagrange.move(30, 50)

        btn_bezier = QtWidgets.QPushButton("Bezier", self)
        btn_bezier.move(150, 50)

        btn_hermite = QtWidgets.QPushButton("Hermite", self)
        btn_hermite.move(30, 110)

        btn_cubic_spline = QtWidgets.QPushButton("Cubic Spline", self)
        btn_cubic_spline.move(150, 110)
      
        btn_close = QtWidgets.QPushButton("Close", self)
        btn_close.move(150, 160)
      
        btn_lagrange.clicked.connect(self.buttonClicked)            
        btn_bezier.clicked.connect(self.buttonClicked)
        btn_hermite.clicked.connect(self.buttonClicked)            
        btn_cubic_spline.clicked.connect(self.buttonClicked)
        btn_close.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('Application Main Menu')
        self.show()
        
    def buttonClicked(self):
        from midterm import main_window
        sender = self.sender()
        if sender.text() == "Lagrange":
            print("Lagrange Selected.")
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

    def menu_window(self):
        self.switch_window.emit()



class Controller:

    def __init__(self):
        self.menu_window = MenuClass()

        
    def show_menu_window(self):
        self.menu_window = MenuClass()
        self.menu_window.show()

    def show_main(self):
        self.window = MainWindow()
        self.menu_window.close()
        self.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_menu_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()