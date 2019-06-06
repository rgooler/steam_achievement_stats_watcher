# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_AddGame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddGame(object):
    def setupUi(self, AddGame):
        AddGame.setObjectName("AddGame")
        AddGame.resize(670, 381)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGame.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AddGame)
        self.centralwidget.setObjectName("centralwidget")
        AddGame.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddGame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        AddGame.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddGame)
        self.statusbar.setObjectName("statusbar")
        AddGame.setStatusBar(self.statusbar)

        self.retranslateUi(AddGame)
        QtCore.QMetaObject.connectSlotsByName(AddGame)

    def retranslateUi(self, AddGame):
        _translate = QtCore.QCoreApplication.translate
        AddGame.setWindowTitle(_translate("AddGame", "Add Game/cheevos"))

