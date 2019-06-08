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
        self.widget = QtWidgets.QWidget(AddGame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 514, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.games = QtWidgets.QListWidget(self.splitter)
        self.games.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.games.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.games.setProperty("showDropIndicator", False)
        self.games.setAlternatingRowColors(False)
        self.games.setResizeMode(QtWidgets.QListView.Adjust)
        self.games.setObjectName("games")
        self.listWidget_2 = QtWidgets.QListWidget(self.splitter)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_2.setAlternatingRowColors(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.splitter)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(AddGame)
        QtCore.QMetaObject.connectSlotsByName(AddGame)

    def retranslateUi(self, AddGame):
        _translate = QtCore.QCoreApplication.translate
        AddGame.setWindowTitle(_translate("AddGame", "Add Game"))
        self.pushButton.setText(_translate("AddGame", "Add Games"))

