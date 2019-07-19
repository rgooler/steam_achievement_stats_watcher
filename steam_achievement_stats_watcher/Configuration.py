import sys
from PyQt5.QtWidgets import QDialog, qApp
import steam_achievement_stats_watcher
from PyQt5.QtCore import QSettings
import ui


class Configuration(QDialog):
    pass


class Ui_Configuration(ui.Ui_Configuration):
    def setupUi(self, Configuration):
        super().setupUi(Configuration)
        self.dialog = Configuration
        settings = QSettings()
        self.ApiKey.setText(settings.value('ApiKey', type=str))
        self.SteamID64.setText(settings.value('SteamID64', type=str))
        self.UpdateInterval.setProperty("value", settings.value('UpdateInterval', type=int, defaultValue=15))
        gamelist = [str(i) for i in settings.value('WatchedGames', type=list, defaultValue=[]) if i]
        print(gamelist)
        self.watchedGames.setText(",".join(gamelist))
        self.configButtonBox.accepted.connect(self.accept)
        self.configButtonBox.rejected.connect(Configuration.reject)

    def accept(self):
        settings = QSettings()
        settings.setValue('ApiKey', self.ApiKey.text())
        settings.setValue('SteamID64', self.SteamID64.text())
        settings.setValue('UpdateInterval', self.UpdateInterval.value())
        settings.setValue('WatchedGames', self.watchedGames.text().split(','))
        settings.sync()
        self.dialog.accept()
