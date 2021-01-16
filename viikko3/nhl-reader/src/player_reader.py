import requests
from player import Player

class PlayerReader():
    def __init__(self, url):
        self.__url = url

    def get_players(self):
        response = requests.get(self.__url).json()
        players = []

        for player_dict in response:
            players.append(Player(
                player_dict["name"],
                player_dict["team"],
                player_dict["goals"],
                player_dict["assists"],
                player_dict["nationality"],
                ))

        return players


