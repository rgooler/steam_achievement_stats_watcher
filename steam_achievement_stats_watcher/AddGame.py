import sys
from PyQt5.QtWidgets import QDialog, QListWidget, QListWidgetItem
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings
import ui


class AddGame(QDialog):
    pass


class Ui_AddGame(ui.Ui_AddGame):
    def setupUi(self, AddGame):
        super().setupUi(AddGame)
        self.dialog = AddGame
        # Load data
        settings = QSettings()
        sd = steam_achievement_stats_watcher.steamdata()
        sd.load_games()
        # Setup game list
        self.games.setSortingEnabled(True)
        for appid, game in sd.usergames.items():
            self.games.addItem(game)
        # self.games.sortItems()
        self.games.show()
