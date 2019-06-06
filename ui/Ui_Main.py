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
        Main.resize(511, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 505, 240))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 158, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddGameButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.AddGameButton.setObjectName("AddGameButton")
        self.horizontalLayout.addWidget(self.AddGameButton)
        self.ConfigureButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ConfigureButton.setObjectName("ConfigureButton")
        self.horizontalLayout.addWidget(self.ConfigureButton)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Steam Achievement Stats Watcher by Jippen"))
        self.pushButton.setText(_translate("Main", "PushButton"))
        self.AddGameButton.setText(_translate("Main", "Add Game"))
        self.ConfigureButton.setText(_translate("Main", "Configure"))

