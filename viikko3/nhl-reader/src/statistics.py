class Statistics():
    def __init__(self, player_reader):
        self.__player_reader = player_reader
        self.__players = self.__player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = filter(lambda player: player.nationality == nationality, self.__players)

        return sorted(
                list(players), reverse = True, key = lambda player: player.score)
