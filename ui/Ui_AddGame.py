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
        AddGame.resize(532, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddGame.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(AddGame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 514, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
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
        self.verticalLayout.addWidget(self.splitter)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(AddGame)
        QtCore.QMetaObject.connectSlotsByName(AddGame)

    def retranslateUi(self, AddGame):
        _translate = QtCore.QCoreApplication.translate
        AddGame.setWindowTitle(_translate("AddGame", "Add Game"))
        self.pushButton.setText(_translate("AddGame", "Add Games"))

