# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 480, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 10, 61, 16))
        self.label_4.setObjectName("label_4")
        self.browseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.browseBtn.setGeometry(QtCore.QRect(380, 70, 93, 28))
        self.browseBtn.setObjectName("browseBtn")
        self.postBtn = QtWidgets.QPushButton(self.centralwidget)
        self.postBtn.setGeometry(QtCore.QRect(700, 40, 93, 28))
        self.postBtn.setObjectName("postBtn")
        self.postTbl = QtWidgets.QTableWidget(self.centralwidget)
        self.postTbl.setGeometry(QtCore.QRect(400, 110, 671, 431))
        self.postTbl.setRowCount(50)
        self.postTbl.setColumnCount(5)
        self.postTbl.setObjectName("postTbl")
        self.usernameTbl = QtWidgets.QTableWidget(self.centralwidget)
        self.usernameTbl.setGeometry(QtCore.QRect(30, 40, 171, 401))
        self.usernameTbl.setRowCount(50)
        self.usernameTbl.setColumnCount(1)
        self.usernameTbl.setObjectName("usernameTbl")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(500, 40, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 480, 139, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.usernameLn = QtWidgets.QLineEdit(self.layoutWidget)
        self.usernameLn.setObjectName("usernameLn")
        self.verticalLayout.addWidget(self.usernameLn)
        self.passwordLn = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordLn.setObjectName("passwordLn")
        self.verticalLayout.addWidget(self.passwordLn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(260, 480, 95, 65))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_2.addWidget(self.addBtn)
        self.delBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.delBtn.setObjectName("delBtn")
        self.verticalLayout_2.addWidget(self.delBtn)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(210, 40, 283, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.captionLn = QtWidgets.QLineEdit(self.layoutWidget2)
        self.captionLn.setObjectName("captionLn")
        self.horizontalLayout.addWidget(self.captionLn)
        self.fileLn = QtWidgets.QLineEdit(self.layoutWidget2)
        self.fileLn.setObjectName("fileLn")
        self.horizontalLayout.addWidget(self.fileLn)
        self.delPostBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delPostBtn.setGeometry(QtCore.QRect(960, 550, 93, 28))
        self.delPostBtn.setObjectName("delPostBtn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(430, 550, 175, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.filterPostBtn = QtWidgets.QPushButton(self.widget)
        self.filterPostBtn.setObjectName("filterPostBtn")
        self.horizontalLayout_2.addWidget(self.filterPostBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoPostApp"))
        self.label.setText(_translate("MainWindow", "Username :"))
        self.label_2.setText(_translate("MainWindow", "Password :"))
        self.label_3.setText(_translate("MainWindow", "  Caption"))
        self.label_4.setText(_translate("MainWindow", "     File"))
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.postBtn.setText(_translate("MainWindow", "Post"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.delBtn.setText(_translate("MainWindow", "Del"))
        self.delPostBtn.setText(_translate("MainWindow", "Del"))
        self.filterPostBtn.setText(_translate("MainWindow", "Filter"))
