import sys
from PyQt5.QtWidgets import QDialog, qApp, QTableWidgetItem
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings
import ui


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.sd = steam_achievement_stats_watcher.steamdata()
        self.main = Ui_Main()
        self.main.setupUi(self)
        self.show()
        self.sd.update()

    def config_window(self):
        widget = steam_achievement_stats_watcher.Configuration(self)
        dialog = steam_achievement_stats_watcher.Ui_Configuration()
        dialog.setupUi(widget)
        widget.exec_()
        widget.show()
        settings = QSettings()
        self.main.refresh()

    def addgame_window(self):
        widget = steam_achievement_stats_watcher.AddGame(self)
        dialog = steam_achievement_stats_watcher.Ui_AddGame()
        dialog.setupUi(widget)
        widget.exec_()
        widget.show()
        self.main.refresh()


class Ui_Main(ui.Ui_Main):
    data = []

    def setupUi(self, Main):
        print("SETUP_UI")
        super().setupUi(Main)
        self.dialog = Main
        self.AddGameButton.pressed.connect(self.dialog.addgame_window)
        self.ConfigureButton.pressed.connect(self.dialog.config_window)
        self.refresh()

    def refresh(self):
        print("REFRESH")
        self.data = []
        settings = QSettings()
        print(1)
        # Disable add games button without api key & steam ID configured
        self.AddGameButton.setEnabled(
            settings.value('ApiKey', type=str) != "" and
            settings.value('SteamID64', type=str) != ""
        )
        print(2)
        self.stats.clear()
        print(3)
        # Refresh stats
        counter = 0
        print(4)
        self.stats.setRowCount(10000)
        print(5)
        gamelist = settings.value('WatchedGames', type=list)
        print("Got game list:")
        print(gamelist)
        for game in gamelist:
            print(f">> {game}")
            self.get_game_data(game)
        print(f"6 --> {counter}")

        self.stats.setRowCount(len(self.data))
        counter = 0
        for row in self.data:
            self.stats.setItem(counter, 0, QTableWidgetItem(row[0]))
            self.stats.setItem(counter, 1, QTableWidgetItem(row[1]))
            self.stats.setItem(counter, 2, QTableWidgetItem(row[2]))
            counter += 1
        self.stats.resizeColumnToContents(0)
        self.stats.resizeColumnToContents(1)
        self.stats.show()

    def get_game_data(self, appid):
        print(f"GET_GAME_DATA -- {appid}")
        if appid == '':
            return
        try:
            print("try")
            data = []
            print(appid)
            stats = self.dialog.sd.get_game_stats(appid)
            print(stats)
            for stat in stats['playerstats']['stats']:
                print(f"{stats['playerstats']['gameName']} - {stat}")
                l = []
                l.append(stats['playerstats']['gameName'])
                l.append(stat['name'])
                l.append(f"{stat['value']}")
                self.data.append(l)
        except KeyError:
            return
