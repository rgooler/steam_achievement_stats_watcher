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
        AddGame.resize(534, 347)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGame.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddGame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(AddGame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.games = QtWidgets.QListWidget(self.splitter)
        self.games.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.games.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.games.setProperty("showDropIndicator", False)
        self.games.setAlternatingRowColors(False)
        self.games.setResizeMode(QtWidgets.QListView.Adjust)
        self.games.setObjectName("games")
        self.stats = QtWidgets.QListWidget(self.splitter)
        self.stats.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stats.setAlternatingRowColors(True)
        self.stats.setObjectName("stats")
        self.verticalLayout_2.addWidget(self.splitter)
        self.pushButton = QtWidgets.QPushButton(AddGame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(AddGame)
        QtCore.QMetaObject.connectSlotsByName(AddGame)

    def retranslateUi(self, AddGame):
        _translate = QtCore.QCoreApplication.translate
        AddGame.setWindowTitle(_translate("AddGame", "Add Game"))
        self.pushButton.setText(_translate("AddGame", "Add Games"))

