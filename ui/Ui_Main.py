# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setWindowModality(QtCore.Qt.WindowModal)
        Main.resize(703, 479)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddGameButton = QtWidgets.QPushButton(Main)
        self.AddGameButton.setObjectName("AddGameButton")
        self.horizontalLayout.addWidget(self.AddGameButton)
        self.ConfigureButton = QtWidgets.QPushButton(Main)
        self.ConfigureButton.setObjectName("ConfigureButton")
        self.horizontalLayout.addWidget(self.ConfigureButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stats = QtWidgets.QTableWidget(Main)
        self.stats.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.stats.setAlternatingRowColors(True)
        self.stats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.stats.setColumnCount(3)
        self.stats.setObjectName("stats")
        self.stats.setRowCount(0)
        self.stats.horizontalHeader().setVisible(False)
        self.stats.horizontalHeader().setCascadingSectionResizes(False)
        self.stats.horizontalHeader().setHighlightSections(False)
        self.stats.horizontalHeader().setSortIndicatorShown(False)
        self.stats.horizontalHeader().setStretchLastSection(True)
        self.stats.verticalHeader().setVisible(False)
        self.stats.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.stats)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Steam Achievement Stats Watcher by Jippen"))
        self.AddGameButton.setText(_translate("Main", "Add Game"))
        self.ConfigureButton.setText(_translate("Main", "Configure"))
        self.stats.setSortingEnabled(True)
