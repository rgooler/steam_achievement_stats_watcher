import requests
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QCoreApplication
import time
import os.path
import json
import steam_achievement_stats_watcher
import os

basepath = "steam_achievement_stats_watcher/data"
sd = steam_achievement_stats_watcher.steamdata()
sd.load_games()
for filename in os.listdir(basepath):
    with open(f"{basepath}/{filename}") as fh:
        print(filename)
        game = json.load(fh)
    sd.updater_add_game(filename, game)

sd.save()
