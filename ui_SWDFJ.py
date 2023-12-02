# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SWDFJEXgowg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(595, 440)
        MainWindow.setMinimumSize(QSize(595, 440))
        MainWindow.setMaximumSize(QSize(595, 440))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -10, 591, 451))
        self.widget.setStyleSheet(u"\n"
"background-color: rgb(252, 237, 218);\n"
"")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 10, 591, 131))
        self.widget_2.setStyleSheet(u"QWidget\n"
"{\n"
" \n"
"	background-color: rgb(47, 60, 126);\n"
"   border-radius:20%;\n"
"}")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 100, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(52, 205, 220 );\n"
"	\n"
"	color: rgb(222, 184, 135);\n"
"	border-radius:10%;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(37,150,190);\n"
"	color: rgb(255, 255, 255);\n"
"}background-color:rgb(37,150,190);\n"
"	color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 70, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(52, 205, 220 );\n"
"	\n"
"	color: rgb(222, 184, 135);\n"
"	border-radius:10%;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(37,150,190);\n"
"	color: rgb(255, 255, 255);\n"
"}background-color:rgb(37,150,190);\n"
"	color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(470, 40, 75, 23))
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(52, 205, 220 );\n"
"	\n"
"	color: rgb(222, 184, 135);\n"
"	border-radius:10%;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(37,150,190);\n"
"	color: rgb(255, 255, 255);\n"
"}background-color:rgb(37,150,190);\n"
"	color: rgb(255, 255, 255);")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 20, 141, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(222, 184, 135);")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 70, 61, 16))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(222, 184, 135);")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 110, 47, 14))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 100, 51, 16))
        self.label_4.setFont(font1)
        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(190, 70, 191, 21))
        self.progressBar.setStyleSheet(u"color: rgb(222, 184, 135);\n"
"background-color: rgb(255, 255, 255);")
        self.progressBar.setValue(24)
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(90, 170, 361, 192))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"RESUME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SCRAPPING", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#deb887;\">Time</span></p></body></html>", None))
    # retranslateUi

