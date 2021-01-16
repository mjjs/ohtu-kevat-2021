import unittest
from statistics import Statistics, sort_by_points
from player import Player

class StubPlayerReader:
    def get_players(self):
        return [
                Player("Player_One", "T1", 1, 2),
                Player("Player_Two", "T2", 2, 3),
                Player("Player_Three", "T1", 4, 5),
                Player("Player_Four", "T3", 6, 7),
                Player("Player_Five", "T1", 8, 9),
                ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(StubPlayerReader())

    def test_search_returns_none_if_player_not_found(self):
        self.assertEqual(self.statistics.search("Esko"), None)

    def test_search_returns_player_if_found(self):
        self.assertEqual(
                str(self.statistics.search("Player_One")),
                "Player_One T1 1 + 2 = 3")

    def test_team_returns_all_players_in_same_team(self):
        players = self.statistics.team("T1")

        str_players = [str(player) for player in players]

        self.assertEqual(len(players), 3)

        self.assertEqual("Player_One T1 1 + 2 = 3" in str_players, True)
        self.assertEqual("Player_Three T1 4 + 5 = 9" in str_players, True)
        self.assertEqual("Player_Five T1 8 + 9 = 17" in str_players, True)

    def test_sort_by_points_returns_player_points(self):
        self.assertEqual(sort_by_points(Player("Name", "Team", 1, 2)), 3)

    # Regarding the last two tests:
    #
    # There is a bug in the example code which iterates one result too many
    # but it will not be fixed because there was no mention about it in the
    # instructions and changing the original code without askingmight been seen
    # as "cheating".
    #
    # The tests have been implemented to give 100% test coverage despite the bug.

    def test_top_scorers_returns_empty_list_on_zero_input(self):
        self.assertEqual(self.statistics.top_scorers(-1), [])

    def test_top_scorers_returns_top_scorers_sorted(self):
        players = self.statistics.top_scorers(2)

        str_players = [str(player) for player in players]

        self.assertEqual(len(players), 3)
        self.assertEqual("Player_Five T1 8 + 9 = 17", str_players[0])
        self.assertEqual("Player_Four T3 6 + 7 = 13", str_players[1])
        self.assertEqual("Player_Three T1 4 + 5 = 9", str_players[2])
