import sys
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QTableWidgetItem
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings, Qt
import ui


class AddGame(QDialog):
    pass


class Ui_AddGame(ui.Ui_AddGame):
    statsHeader = ['Key', 'Value']

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
        self.pushButton.clicked.connect(self.accept)
        self.games.show()

    def list_game_stats(self):
        current_game = self.games.currentItem()
        self.stats.clear()
        try:
            data = []
            appid = self.sd.get_appid(current_game.text())
            print(appid)
            stats = self.sd.get_game_stats(appid)
            print(stats)
            counter = 0
            self.stats.setRowCount(len(stats['playerstats']['stats']))
            for stat in stats['playerstats']['stats']:
                print(stat)
                self.stats.setItem(counter, 0, QTableWidgetItem(stat['name']))
                self.stats.setItem(counter, 1, QTableWidgetItem(f"{stat['value']}"))
                counter += 1
        except KeyError:
            self.stats.setRowCount(1)
            self.stats.setItem(counter, 0, QTableWidgetItem("No stats available"))
        self.stats.show()

    def accept(self):
        current_game = self.games.currentItem()
        appid = self.sd.get_appid(current_game.text())
        print(f"Adding {appid}")
        settings = QSettings()
        l = settings.value('WatchedGames', type=list)
        print(f"l: {l}")
        l.append(appid)
        print(f"l:: {l}")
        settings.setValue('WatchedGames', l)
        settings.sync()
        self.dialog.accept()
