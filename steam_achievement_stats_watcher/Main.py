import sys
from PyQt5.QtWidgets import QDialog, qApp
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings
import ui


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.main = Ui_Main()
        self.main.setupUi(self)
        self.show()

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
    def setupUi(self, Main):
        super().setupUi(Main)
        self.dialog = Main
        self.AddGameButton.pressed.connect(self.dialog.addgame_window)
        self.ConfigureButton.pressed.connect(self.dialog.config_window)
        self.refresh()

    def refresh(self):
        settings = QSettings()
        # Disable add games button without api key & steam ID configured
        self.AddGameButton.setEnabled(
            settings.value('ApiKey', type=str) != "" and
            settings.value('SteamID64', type=str) != ""
        )
