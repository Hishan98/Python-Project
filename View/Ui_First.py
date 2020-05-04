# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 689)
        MainWindow.setStyleSheet("background-color: #1A1D3A;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(0, 540, 981, 41))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status.setStyleSheet("color:white;")
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(0, 170, 991, 271))
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("D:/Hishan-Projects & stuff/Photoshop work/PNG\'s & Templates/pngpicture.com_34066.png"))
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Talk & shop", "Talk & shop"))
        self.Status.setText(_translate("txt 1", "Listening."))
        self.Status.setText(_translate("txt2", "Pakoo."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
