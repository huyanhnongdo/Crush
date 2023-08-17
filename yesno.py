from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Crush")
        MainWindow.setWindowTitle("Crush")
        MainWindow.resize(640, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(70, 110, 161, 101))
        self.yes_button.setObjectName("yes_button")
        self.no_button = QtWidgets.QPushButton(self.centralwidget)
        self.no_button.setGeometry(QtCore.QRect(380, 110, 161, 101))
        self.no_button.setObjectName("no_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 301, 71))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setIndent(125)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crush"))
        self.yes_button.setText(_translate("MainWindow", "Có"))
        self.no_button.setText(_translate("MainWindow", "Không"))
        self.label.setText(_translate("MainWindow", "Love Me?"))
        self.no_button.enterEvent = self.onButtonEnter
        self.no_button.leaveEvent = self.onButtonLeave
        self.yes_button.clicked.connect(self.show_message)
    def onButtonEnter(self, event):
        self.no_button.setText('Có')
        self.yes_button.setText('Không')

        
    def onButtonLeave(self, event):
        self.no_button.setText('Không')
        self.yes_button.setText('Có')
    
    def show_message(self):
        msg = QMessageBox()
        msg.setText("I know that =))))")
        msg.setWindowTitle("HuyAnhDz")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
