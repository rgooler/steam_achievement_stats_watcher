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
        Configuration.setWindowModality(QtCore.Qt.WindowModal)
        Configuration.resize(258, 122)
        Configuration.setMinimumSize(QtCore.QSize(258, 122))
        Configuration.setMaximumSize(QtCore.QSize(258, 122))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Configuration.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(Configuration)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 258, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.ApiKeyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ApiKeyLabel.setToolTip("")
        self.ApiKeyLabel.setTextFormat(QtCore.Qt.AutoText)
        self.ApiKeyLabel.setOpenExternalLinks(True)
        self.ApiKeyLabel.setObjectName("ApiKeyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ApiKeyLabel)
        self.ApiKey = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ApiKey.setObjectName("ApiKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ApiKey)
        self.UpdateInterval = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.UpdateInterval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UpdateInterval.setMinimum(1)
        self.UpdateInterval.setMaximum(3600)
        self.UpdateInterval.setProperty("value", 15)
        self.UpdateInterval.setObjectName("UpdateInterval")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.UpdateInterval)
        self.UpdateIntervalLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.UpdateIntervalLabel.setObjectName("UpdateIntervalLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.UpdateIntervalLabel)
        self.SteamID64Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.SteamID64Label.setObjectName("SteamID64Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SteamID64Label)
        self.SteamID64 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SteamID64.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.SteamID64.setClearButtonEnabled(False)
        self.SteamID64.setObjectName("SteamID64")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SteamID64)
        self.configButtonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.configButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.configButtonBox.setObjectName("configButtonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.configButtonBox)

        self.retranslateUi(Configuration)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Configuration"))
        self.ApiKeyLabel.setText(_translate("Configuration", "<html><head/><body><p><a href=\"https://steamcommunity.com/dev/apikey\"><span style=\" text-decoration: underline; color:#0000ff;\">Web API Key</span></a></p></body></html>"))
        self.UpdateInterval.setSuffix(_translate("Configuration", " seconds"))
        self.UpdateIntervalLabel.setToolTip(_translate("Configuration", "<html><head/><body><p>This value is how many seconds the app will wait between API calls to update steam stats. Too fast may result in temporary API Blocking.</p></body></html>"))
        self.UpdateIntervalLabel.setText(_translate("Configuration", "Update Interval"))
        self.SteamID64Label.setText(_translate("Configuration", "Steam ID64"))

