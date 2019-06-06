# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(608, 496)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        self.AddGame = QtWidgets.QMenu(self.menubar)
        self.AddGame.setObjectName("AddGame")
        self.Configure = QtWidgets.QMenu(self.menubar)
        self.Configure.setObjectName("Configure")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.menubar.addAction(self.AddGame.menuAction())
        self.menubar.addAction(self.Configure.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Steam Achievement Stats Watcher by Jippen"))
        self.pushButton.setText(_translate("Main", "PushButton"))
        self.AddGame.setTitle(_translate("Main", "Add Game"))
        self.Configure.setTitle(_translate("Main", "Configure"))

