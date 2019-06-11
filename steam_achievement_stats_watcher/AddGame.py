import sys
from PyQt5.QtWidgets import QDialog, QListWidget, QListWidgetItem
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings, Qt
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
            item = QListWidgetItem(game)
            if str(appid) in self.sd.data.keys():
                if self.sd.data[str(appid)]['hasStats'] is False:
                    # Skip games with known no stats
                    continue
            # Now that all flags are set, add to the list
            self.games.addItem(game)
        self.games.currentItemChanged.connect(self.list_game_stats)
        self.games.show()

    def list_game_stats(self):
        current_game = self.games.currentItem()
        try:
            appid = self.sd.get_appid(current_game.text())
            print(appid)
            stats = self.sd.get_game_stats(appid)
            print(stats)
            self.stats.clear()
            for stat in stats['playerstats']['stats']:
                print(stat)
                item = QListWidgetItem(stat['name'])
                item.setSelected(True)
                self.stats.addItem(item)
            self.stats.show()
        except KeyError:
            self.stats.clear()
            self.stats.addItem(f"No stats available for {current_game.text()}")
            self.stats.show()
