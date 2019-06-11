import requests
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QCoreApplication
import time
import os.path
import json


class steamdata(object):
    allgames = {}
    usergames = {}
    data = None
    __datafile = "data.json"

    def load_games(self):
        if self.allgames == {}:
            self.__get_all_steam_games()
        if self.usergames == {}:
            self.__get_users_games()
        if self.data is None:
            with open(self.__datafile) as fh:
                self.data = json.load(fh)

    def __get_all_steam_games(self):
        url = "https://api.steampowered.com/ISteamApps/GetAppList/v0002/"
        params = {"format": "json"}
        r = requests.get(url, params=params)
        for app in r.json()['applist']['apps']:
            self.allgames[app['appid']] = app['name']

    def __get_users_games(self):
        settings = QSettings()
        url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        params = {
            "key": settings.value('ApiKey', type=str),
            "steamid": settings.value('SteamID64', type=str),
            "format": "json"
        }
        if params['key'] != "" and params['steamid'] != "":
            r = requests.get(url, params=params)
            for game in r.json()['response']['games']:
                self.usergames[game['appid']] = self.allgames[game['appid']]

    def get_game_stats(self, appid):
        settings = QSettings()
        url = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"
        params = {
            "key": settings.value('ApiKey', type=str),
            "steamid": settings.value('SteamID64', type=str),
            "appid": appid,
            "format": "json"
        }
        if params['key'] != "" and params['steamid'] != "":
            r = requests.get(url, params=params)
            return r.json()

    def updater(self):
        self.load_games()
        counter = 0
        for appid, name in self.allgames.items():
            try:
                if str(appid) not in self.data.keys():
                    counter = counter + 1
                    print(f"{appid} - {name}")
                    data = self.get_game_stats(appid)
                    self.updater_add_game(appid, data)
                    # Safety save every 10 games
                    if counter % 10 == 0:
                        self.save()
            except requests.exceptions.ConnectionError:
                time.sleep(10)
        self.save()

    def updater_add_game(self, appid, game):
        data = {}
        data['hasStats'] = False
        data['hasAchievementStats'] = False
        if 'playerstats' in game.keys():
            if 'stats' in game['playerstats'].keys():
                # Return true if not an empty dict
                contents = bool(len(game['playerstats']['stats']))
                data['hasStats'] = contents
            if 'achievements' in game['playerstats'].keys():
                # Return true if not an empty dict
                contents = bool(len(game['playerstats']['achievements']))
                data['hasAchievementStats'] = contents
        self.data[appid] = data

    def save(self):
        with open(self.__datafile, "w") as fh:
            json.dump(self.data, fh, indent=2)

    def update(self):
        settings = QSettings()
        url = "https://rgooler.github.io/steam_achievement_stats_watcher/data.json.zip"
        r = requests.head(url)
        if r.headers['etag'] != settings.value('etag', type=str):
            # Update available! Download it!
            with open("data.json.zip", 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
            # Save etag
            settings.setValue('etag', r.headers['etag'])
