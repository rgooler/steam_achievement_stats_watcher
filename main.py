import steam_achievement_stats_watcher
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, QSettings, QTimer
import sys


if __name__ == "__main__":
    QCoreApplication.setApplicationName("Jippen")
    QCoreApplication.setOrganizationDomain("bullshit.website")
    QCoreApplication.setApplicationName("Steam Achievement Stats Watcher")

    app = QApplication(sys.argv)
    w = steam_achievement_stats_watcher.Main()

    settings = QSettings()
    timer = QTimer()
    timer.timeout.connect(w.main.refresh)
    timer.start(settings.value('UpdateInterval', type=int, defaultValue=15) * 1000)

    w.show()
    sys.exit(app.exec_())
