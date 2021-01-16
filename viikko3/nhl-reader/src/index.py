from player import Player
from player_reader import PlayerReader
from statistics import Statistics

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    statistics = Statistics(reader)

    players = statistics.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
