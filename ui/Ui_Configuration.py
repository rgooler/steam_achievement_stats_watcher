# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Configuration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.resize(239, 141)
        Configuration.setMinimumSize(QtCore.QSize(239, 141))
        Configuration.setMaximumSize(QtCore.QSize(239, 141))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Configuration.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(Configuration)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 217, 74))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.ApiKeyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ApiKeyLabel.setObjectName("ApiKeyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ApiKeyLabel)
        self.ApiKey = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ApiKey.setObjectName("ApiKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ApiKey)
        self.UpdateFrequency = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.UpdateFrequency.setObjectName("UpdateFrequency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.UpdateFrequency)
        self.UpdateFrequencyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.UpdateFrequencyLabel.setObjectName("UpdateFrequencyLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.UpdateFrequencyLabel)
        self.SteamID64Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.SteamID64Label.setObjectName("SteamID64Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SteamID64Label)
        self.SteamID64 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SteamID64.setObjectName("SteamID64")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SteamID64)
        self.configButtonBox = QtWidgets.QDialogButtonBox(Configuration)
        self.configButtonBox.setGeometry(QtCore.QRect(70, 100, 156, 23))
        self.configButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.configButtonBox.setObjectName("configButtonBox")

        self.retranslateUi(Configuration)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Configuration"))
        self.ApiKeyLabel.setToolTip(_translate("Configuration", "<html><head/><body><p><a href=\"https://steamcommunity.com/dev/apikey\"><span style=\" text-decoration: underline; color:#0000ff;\">Get a steam web api key here</span></a></p></body></html>"))
        self.ApiKeyLabel.setText(_translate("Configuration", "Web API Key"))
        self.UpdateFrequencyLabel.setToolTip(_translate("Configuration", "<html><head/><body><p>This value is how many seconds the app will wait between API calls to update steam stats. Too fast may result in temporary API Blocking.</p></body></html>"))
        self.UpdateFrequencyLabel.setText(_translate("Configuration", "Update Interval"))
        self.SteamID64Label.setText(_translate("Configuration", "Steam ID64"))

