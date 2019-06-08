import requests
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QCoreApplication


class steamdata(object):
    allgames = {}
    usergames = {}

    def load_games(self):
        self.__get_all_steam_games()
        self.__get_users_games()

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
            return r.json()['playerstats']

if __name__ == "__main__":
    QCoreApplication.setApplicationName("Jippen")
    QCoreApplication.setOrganizationDomain("bullshit.website")
    QCoreApplication.setApplicationName("Steam Achievement Stats Watcher")

    sd = steamdata()
    games = list(sd.usergames.values())
    print(games[0])
    print(len(games))
    print(sd.get_game_stats(398850)['stats'])
