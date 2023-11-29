import os

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QWidget

from algo import *
from data import *

DEFAULT_READ_FILE = os.path.join(os.getcwd(), "source_file.csv")
DEFAULT_WRITE_FILE = os.path.join(os.getcwd(), "answer.csv")


class Ui_MarksCounter(QWidget):
    def setupUi(self, MarkCounter):
        self.readFile = DEFAULT_READ_FILE
        self.writeFile = DEFAULT_WRITE_FILE

        MarkCounter.setObjectName("MarkCounter")
        MarkCounter.resize(490, 340)
        MarkCounter.setEnabled(True)
        MarkCounter.setStyleSheet("background-color: rgb(183, 212, 225)")
        self.centralwidget = QtWidgets.QWidget(MarkCounter)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 10, 490, 40))
        self.title.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(84, 84, 114);")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.inputPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputPathLabel.setGeometry(QtCore.QRect(25, 100, 320, 40))
        self.inputPathLabel.setStyleSheet("color: rgb(226, 239, 239);\n"
                                          "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                          "background-color: rgb(100, 121, 155);")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputPathLabel.setObjectName("inputPathLabel")
        self.outputPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputPathLabel.setGeometry(QtCore.QRect(25, 185, 320, 40))
        self.outputPathLabel.setStyleSheet("color: rgb(226, 239, 239);\n"
                                           "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                           "text-align: center;\n"  # пока не работает
                                           "background-color: rgb(100, 121, 155);")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outputPathLabel.setObjectName("outputPathLabel")
        self.sortTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.sortTimeLabel.setGeometry(QtCore.QRect(25, 270, 320, 40))
        self.sortTimeLabel.setStyleSheet("color: rgb(226, 239, 239);\n"
                                         "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                         "text-align: center;\n"
                                         "background-color: rgb(100, 121, 155);")
        self.sortTimeLabel.setText("")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sortTimeLabel.setObjectName("sortTimeLabel")

        self.changeInputBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeInputBtn.setGeometry(QtCore.QRect(365, 100, 100, 40))
        self.changeInputBtn.setStyleSheet("background-color: rgb(84, 84, 114);\n"
                                          "color: rgb(226, 239, 239);\n"
                                          "font: 75 italic 10pt \"Noto Sans\";\n"
                                          "border: 1px solid rgb(84, 84, 114);\n"
                                          "border-radius: 10px;")
        self.changeInputBtn.setObjectName("changeInputBtn")

        self.changeOutputBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeOutputBtn.setGeometry(QtCore.QRect(365, 185, 100, 40))
        self.changeOutputBtn.setStyleSheet("background-color: rgb(84, 84, 114);\n"
                                           "color: rgb(226, 239, 239);\n"
                                           "font: 75 italic 10pt \"Noto Sans\";\n"
                                           "border: 1px solid rgb(84, 84, 114);\n"
                                           "border-radius: 10px;")

        self.changeOutputBtn.setObjectName("changeOutputBtn")
        self.sortBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sortBtn.setGeometry(QtCore.QRect(365, 270, 100, 40))
        self.sortBtn.setStyleSheet("background-color: rgb(84, 84, 114);\n"
                                   "color: rgb(226, 239, 239);\n"
                                   "font: 75 italic 10pt \"Noto Sans\";\n"
                                   "border: 1px solid rgb(84, 84, 114);\n"
                                   "border-radius: 10px;")
        self.sortBtn.setObjectName("sortBtn")

        self.firstComment = QtWidgets.QLabel(self.centralwidget)
        self.firstComment.setGeometry(QtCore.QRect(26, 70, 140, 20))
        self.firstComment.setStyleSheet("color: rgb(76, 79, 119);\n"
                                        "font: 75 11pt \"MS Shell Dlg 2\";")
        self.firstComment.setObjectName("firstComment")

        self.thirdComment = QtWidgets.QLabel(self.centralwidget)
        self.thirdComment.setGeometry(QtCore.QRect(26, 157, 120, 20))
        self.thirdComment.setStyleSheet("color: rgb(76, 79, 119);\n"
                                        "font: 75 11pt \"MS Shell Dlg 2\";")
        self.thirdComment.setObjectName("secondComment_2")
        self.fourthComment = QtWidgets.QLabel(self.centralwidget)
        self.fourthComment.setGeometry(QtCore.QRect(26, 243, 140, 20))
        self.fourthComment.setStyleSheet("color: rgb(76, 79, 119);\n"
                                         "font: 75 11pt \"MS Shell Dlg 2\";")
        self.fourthComment.setObjectName("secondComment_3")
        MarkCounter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MarkCounter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 21))
        self.menubar.setObjectName("menubar")
        MarkCounter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MarkCounter)
        self.statusbar.setObjectName("statusbar")
        MarkCounter.setStatusBar(self.statusbar)

        self.retranslateUi(MarkCounter)
        QtCore.QMetaObject.connectSlotsByName(MarkCounter)

        self.updatePathLabels()

        self.addFunc()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Оценка успеваемости"))
        self.changeInputBtn.setText(_translate("MainWindow", "Change Input"))
        self.changeOutputBtn.setText(_translate("MainWindow", "Change Output"))
        self.sortBtn.setText(_translate("MainWindow", "Sort"))
        self.firstComment.setText(_translate("MainWindow", "Input Path:"))
        self.thirdComment.setText(_translate("MainWindow", "Output Path:"))
        self.fourthComment.setText(_translate("MainWindow", "Рассчитать оценку:"))

    def addFunc(self):
        self.changeInputBtn.clicked.connect(self.chooseInputFile)
        self.changeOutputBtn.clicked.connect(self.chooseOutputFile)
        self.sortBtn.clicked.connect(self.sortArray)

    def chooseInputFile(self):
        fileName = self.askOpenFile(self.readFile)
        if fileName:
            self.readFile = fileName
        self.updatePathLabels()

    def chooseOutputFile(self):
        fileName = self.askWriteFile(self.writeFile)
        if fileName:
            self.writeFile = fileName
        self.updatePathLabels()

    def generateArray(self):
        fileName = self.askWriteFile(self.readFile)
        arrayInit(fileName, 100)
        if not fileName:
            return
        self.readFile = fileName
        self.updatePathLabels()

    def sortArray(self):
        if not os.path.isfile(self.readFile):
            return
        array = readFile(self.readFile)
        self.sortTimeLabel.setText(sortArray(array))
        print(array)
        response = sortArray(array)
        print(response)
        self.sortTimeLabel.setText("Возможная оценка: "+response)

    def askOpenFile(self, defaultPath):
        file_filter = 'Data File (*.csv);; All files (*)'
        pickedFile, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Выберите название файла для сортировки',
            directory=defaultPath,
            filter=file_filter
        )
        return pickedFile if os.path.isfile(pickedFile) else None

    def askWriteFile(self, defaultPath):
        file_filter = 'Data File (*.csv);; All files (*)'
        pickedFile, _ = QFileDialog.getSaveFileName(
            parent=self,
            caption='Выберите название файла для результата',
            directory=defaultPath,
            filter=file_filter
        )
        return pickedFile

    def updatePathLabels(self):
        self.inputPathLabel.setText(self.readFile)
        self.outputPathLabel.setText(self.writeFile)
