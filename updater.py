import steam_achievement_stats_watcher
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, QSettings
import sys
from datetime import datetime
from zipfile import ZipFile, ZIP_BZIP2


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

    print(f"Parsing games...")
    start = datetime.now()
    sd.updater()
    end = datetime.now()
    print(f"Done: {end - start}")

    print(f"Compressing...")
    start = datetime.now()
    with ZipFile("data.json.zip", "w", compression=ZIP_BZIP2, compresslevel=9) as z:
        z.write("data.json")
    end = datetime.now()
    print(f"Done: {end - start}")
