# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Configuration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.setWindowModality(QtCore.Qt.WindowModal)
        Configuration.resize(329, 151)
        Configuration.setMinimumSize(QtCore.QSize(329, 151))
        Configuration.setMaximumSize(QtCore.QSize(329, 151))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Configuration.setWindowIcon(icon)
        self.formLayout_2 = QtWidgets.QFormLayout(Configuration)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ApiKeyLabel = QtWidgets.QLabel(Configuration)
        self.ApiKeyLabel.setToolTip("")
        self.ApiKeyLabel.setTextFormat(QtCore.Qt.AutoText)
        self.ApiKeyLabel.setOpenExternalLinks(True)
        self.ApiKeyLabel.setObjectName("ApiKeyLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ApiKeyLabel)
        self.ApiKey = QtWidgets.QLineEdit(Configuration)
        self.ApiKey.setObjectName("ApiKey")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ApiKey)
        self.SteamID64 = QtWidgets.QLineEdit(Configuration)
        self.SteamID64.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.SteamID64.setClearButtonEnabled(False)
        self.SteamID64.setObjectName("SteamID64")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SteamID64)
        self.SteamID64Label = QtWidgets.QLabel(Configuration)
        self.SteamID64Label.setObjectName("SteamID64Label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.SteamID64Label)
        self.UpdateIntervalLabel = QtWidgets.QLabel(Configuration)
        self.UpdateIntervalLabel.setObjectName("UpdateIntervalLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.UpdateIntervalLabel)
        self.UpdateInterval = QtWidgets.QSpinBox(Configuration)
        self.UpdateInterval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UpdateInterval.setMinimum(1)
        self.UpdateInterval.setMaximum(3600)
        self.UpdateInterval.setProperty("value", 15)
        self.UpdateInterval.setObjectName("UpdateInterval")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.UpdateInterval)
        self.configButtonBox = QtWidgets.QDialogButtonBox(Configuration)
        self.configButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.configButtonBox.setObjectName("configButtonBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.configButtonBox)
        self.watchedGames = QtWidgets.QLineEdit(Configuration)
        self.watchedGames.setObjectName("watchedGames")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.watchedGames)
        self.watchedGamesLabel = QtWidgets.QLabel(Configuration)
        self.watchedGamesLabel.setObjectName("watchedGamesLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.watchedGamesLabel)

        self.retranslateUi(Configuration)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Configuration"))
        self.ApiKeyLabel.setText(_translate("Configuration", "<html><head/><body><p><a href=\"https://steamcommunity.com/dev/apikey\"><span style=\" text-decoration: underline; color:#0000ff;\">Web API Key</span></a></p></body></html>"))
        self.SteamID64Label.setText(_translate("Configuration", "Steam ID64"))
        self.UpdateIntervalLabel.setToolTip(_translate("Configuration", "<html><head/><body><p>This value is how many seconds the app will wait between API calls to update steam stats. Too fast may result in temporary API Blocking.</p></body></html>"))
        self.UpdateIntervalLabel.setText(_translate("Configuration", "Update Interval"))
        self.UpdateInterval.setSuffix(_translate("Configuration", " seconds"))
        self.watchedGamesLabel.setText(_translate("Configuration", "Watched Games"))
