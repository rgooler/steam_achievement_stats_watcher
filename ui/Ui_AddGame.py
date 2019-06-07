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
        AddGame.setWindowModality(QtCore.Qt.WindowModal)
        AddGame.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGame.setWindowIcon(icon)

        self.retranslateUi(AddGame)
        QtCore.QMetaObject.connectSlotsByName(AddGame)

    def retranslateUi(self, AddGame):
        _translate = QtCore.QCoreApplication.translate
        AddGame.setWindowTitle(_translate("AddGame", "Add Game"))

