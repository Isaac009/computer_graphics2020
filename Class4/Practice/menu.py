# # import sys
# # from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
# # from PyQt5.QtGui import QIcon


# # class Example(QMainWindow):
    
# #     def __init__(self):
# #         super().__init__()
        
# #         self.initUI()
        
        
# #     def initUI(self):               
        
# #         textEdit = QTextEdit()
# #         self.setCentralWidget(textEdit)

# #         exitAct = QAction(QIcon('exit.png'), 'Exit', self)
# #         exitAct.setShortcut('Ctrl+Q')
# #         exitAct.setStatusTip('Exit application')
# #         exitAct.triggered.connect(self.close)

# #         self.statusBar()

# #         menubar = self.menuBar()
# #         fileMenu = menubar.addMenu('&File')
# #         fileMenu.addAction(exitAct)

# #         toolbar = self.addToolBar('Exit')
# #         toolbar.addAction(exitAct)
        
# #         self.setGeometry(300, 300, 350, 250)
# #         self.setWindowTitle('Main window')    
# #         self.show()
        
        
# # if __name__ == '__main__':
    
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


# # class Example(QMainWindow):
# #     EXIT_CODE_REBOOT = -123

# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
        
        
# #     def initUI(self):      

# #         btn1 = QPushButton("Lagrang", self)
# #         btn1.move(30, 50)

# #         btn2 = QPushButton("Bezier", self)
# #         btn2.move(150, 50)

# #         btn3 = QPushButton("Hermite", self)
# #         btn3.move(30, 110)

# #         btn4 = QPushButton("Cubic Spline", self)
# #         btn4.move(150, 110)
      
# #         btn1.clicked.connect(self.buttonClicked)            
# #         btn2.clicked.connect(self.buttonClicked)
# #         btn3.clicked.connect(self.buttonClicked)            
# #         btn4.clicked.connect(self.buttonClicked)
        
# #         self.statusBar()
        
# #         self.setGeometry(300, 300, 290, 150)
# #         self.setWindowTitle('Event sender')
# #         self.show()
        
# #     def buttonClicked(self):
      
# #         sender = self.sender()
# #         if sender.text() == "Lagrang":
# #             self.close()
# #             print("Button 1 clicked.")
# #             main_window(mode_v=1)
# #         elif sender.text() == "Bezier":
# #             main_window(mode_v=2)
# #         elif sender.text() == "Hermite":
# #             main_window(mode_v=3)
# #         elif sender.text() == "Cubic Spline":
# #             main_window(mode_v=4)
# #         sf.statusBar().showMessage(sender.text() + ' was pressed')

# class Second(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(Second, self).__init__(parent)


# class First(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(First, self).__init__(parent)
#         self.pushButton = QtGui.QPushButton("click me")

#         self.setCentralWidget(self.pushButton)

#         self.pushButton.clicked.connect(self.on_pushButton_clicked)
#         self.dialogs = list()

#     def on_pushButton_clicked(self):
#         dialog = Second(self)
#         self.dialogs.append(dialog)
#         dialog.show()


# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = First()
#     main.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

import sys
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Switch Window')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Application Main Menu')

        layout = QtWidgets.QGridLayout()

        # self.button = QtWidgets.QPushButton('Login')
        # self.button.clicked.connect(self.login)

        # layout.addWidget(self.button)

        # self.setLayout(layout)

        btn1 = QtWidgets.QPushButton("Lagrang", self)
        btn1.move(30, 50)

        btn2 = QtWidgets.QPushButton("Bezier", self)
        btn2.move(150, 50)

        btn3 = QtWidgets.QPushButton("Hermite", self)
        btn3.move(30, 110)

        btn4 = QtWidgets.QPushButton("Cubic Spline", self)
        btn4.move(150, 110)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)            
        btn4.clicked.connect(self.buttonClicked)
        
        # self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Application Main Menu')
        self.show()
        
    def buttonClicked(self):
        from midterm_v2 import main_window
        sender = self.sender()
        if sender.text() == "Lagrang":
            self.hide()
            print("Lagrang clicked.")
            main_window(mode_v=1)
        elif sender.text() == "Bezier":
            self.hide()
            print("Bezier clicked.")
            main_window(mode_v=2)
        elif sender.text() == "Hermite":
            print("Hermite clicked.")
            main_window(mode_v=3)
        elif sender.text() == "Cubic Spline":
            print("Cubic Spline clicked.")
            main_window(mode_v=4)
        # sf.statusBar().showMessage(sender.text() + ' was pressed')

    def login(self):
        self.switch_window.emit()



class Controller:

    def __init__(self):
        pass
    
    def show_from_hide(self):
        self.login.show()
        
    def show_login(self):
        self.login = Login()
        # self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        # self.login.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()