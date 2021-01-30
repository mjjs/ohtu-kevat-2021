ZERO_POINTS = 0
FIFTEEN_POINTS = 1
THIRTY_POINTS = 2
FORTY_POINTS = 3

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_score(self):
        self.score += 1

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1.increment_score()
        else:
            self.player2.increment_score()

    def get_score(self):
        if self._is_game_even():
            if self.player1.score > FORTY_POINTS:
                return "Deuce"

            score_name = self._get_score_name(self.player1.score)
            return f"{score_name}-All"

        if self.player1.score > FORTY_POINTS or self.player2.score > FORTY_POINTS:
            result = abs(self.player1.score - self.player2.score)

            advantaged_player = self._get_higher_scored_player(self.player1, self.player2)

            if result == 1:
                return f"Advantage {'player1' if advantaged_player == self.player1 else 'player2'}"

            return f"Win for {'player1' if advantaged_player == self.player1 else 'player2'}"

        player1_score_name = self._get_score_name(self.player1.score)
        player2_score_name = self._get_score_name(self.player2.score)

        return f"{player1_score_name}-{player2_score_name}"

    def _get_score_name(self, score):
        if score == ZERO_POINTS:
            return "Love"

        if score == FIFTEEN_POINTS:
            return "Fifteen"

        if score == THIRTY_POINTS:
            return "Thirty"

        return "Forty"

    def _get_higher_scored_player(self, player1, player2):
        return player1 if player1.score > player2.score else player2

    def _is_game_even(self):
        return self.player1.score == self.player2.score
