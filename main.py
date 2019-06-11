import steam_achievement_stats_watcher
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, QSettings
import sys


if __name__ == "__main__":
    QCoreApplication.setApplicationName("Jippen")
    QCoreApplication.setOrganizationDomain("bullshit.website")
    QCoreApplication.setApplicationName("Steam Achievement Stats Watcher")

    steam_achievement_stats_watcher.steamdata.update()

    app = QApplication(sys.argv)
    w = steam_achievement_stats_watcher.Main()
    w.show()
    sys.exit(app.exec_())
