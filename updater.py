import steam_achievement_stats_watcher
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, QSettings
import sys
from datetime import datetime


if __name__ == "__main__":
    QCoreApplication.setApplicationName("Jippen")
    QCoreApplication.setOrganizationDomain("bullshit.website")
    QCoreApplication.setApplicationName("Steam Achievement Stats Watcher")

    sd = steam_achievement_stats_watcher.steamdata()
    print("Loading data...")
    start = datetime.now()
    sd.load_games()
    end = datetime.now()
    print(f"Done: {end - start}")
    sd.updater()
