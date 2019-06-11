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
        self.sd = steam_achievement_stats_watcher.steamdata()
        self.sd.load_games()
        # Setup game list
        self.games.setSortingEnabled(True)
        for appid, game in self.sd.usergames.items():
            self.games.addItem(game)
        self.games.currentItemChanged.connect(self.list_game_stats)
        self.games.show()

    def list_game_stats(self):
        self.stats.addItem("Loading...")
        self.stats.show()
        current_game = self.games.currentItem()
        try:
            stats = self.sd.get_game_stats(current_game.text())
            print(stats)
            self.stats.clear()
            for stat in stats:
                item = QListWidgetItem(stat['name'])
                item.setSelected(True)
                self.stats.addItem(item)
            self.stats.show()
        except KeyError:
            self.stats.clear()
            self.stats.addItem(f"No stats available for {current_game.text()}")
            self.stats.show()
