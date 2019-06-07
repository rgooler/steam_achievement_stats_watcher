import sys
from PyQt5.QtWidgets import QDialog, qApp
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings
import ui


class AddGame(QDialog):
    pass


class Ui_AddGame(ui.Ui_AddGame):
    def setupUi(self, AddGame):
        super().setupUi(AddGame)
        self.dialog = AddGame
        settings = QSettings()
