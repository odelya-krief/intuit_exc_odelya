import unittest

from players import PlayerManager, Player, get_player_manager

player_1 = Player(
    playerID="aardsda01",
    birthYear="1981",
    birthMonth="12",
    birthDay="27",
    birthCountry="USA",
    birthState="CO",
    birthCity="Denver",
    deathYear="",
    deathMonth="",
    deathDay="",
    deathCountry="",
    deathState="",
    deathCity="",
    nameFirst="David",
    nameLast="Aardsma",
    nameGiven="David Allan",
    weight="215",
    height="75",
    bats="R",
    throws="R",
    debut="2004-04-06",
    finalGame="2015-08-23",
    retroID="aardd001",
    bbrefID="aardsda01"
)

player_2 = Player(
    playerID="aaronha01",
    birthYear="1934",
    birthMonth="2",
    birthDay="5",
    birthCountry="USA",
    birthState="AL",
    birthCity="Mobile",
    deathYear="",
    deathMonth="",
    deathDay="",
    deathCountry="",
    deathState="",
    deathCity="",
    nameFirst="Hank",
    nameLast="Aaron",
    nameGiven="Henry Louis",
    weight="180",
    height="72",
    bats="R",
    throws="R",
    debut="1954-04-13",
    finalGame="1976-10-03",
    retroID="aaroh101",
    bbrefID="aaronha01"
)

TEST_PLAYERS_VALID_FILE_PATH = "test_players_valid.csv"
TEST_PLAYERS_EMPTY_FILE_PATH = "test_players_empty.csv"
TEST_PLAYERS_DAMAGED_FILE_PATH = "test_players_damaged.csv"


class TestPlayersManager(unittest.TestCase):
    def test_get_players_returns_all_players(self):
        expected_players = get_player_manager(TEST_PLAYERS_VALID_FILE_PATH).get_players()
        self.assertEqual(expected_players, [player_1, player_2])

    def test_get_players_returns_empty_list_for_empty_csv_file(self):
        expected_players = get_player_manager(TEST_PLAYERS_EMPTY_FILE_PATH).get_players()
        self.assertEqual(expected_players, [])

    def test_get_player_by_id_returns_matching_player(self):
        expected_player = get_player_manager(TEST_PLAYERS_VALID_FILE_PATH).get_player(player_1.playerID)
        self.assertEqual(expected_player, player_1)

    def test_get_player_by_id_returns_None_when_id_was_not_found(self):
        expected_none = get_player_manager(TEST_PLAYERS_VALID_FILE_PATH).get_player("xxx")
        self.assertIsNone(expected_none)

    def test_raise_error_when_file_was_not_found(self):
        self.assertRaises(Exception, lambda: get_player_manager("xxx"))

    def test_raise_error_for_damaged_file(self):
        """
        Expecting TypeError because PlayerManager tries to convert the csv lines to type Player
        but fails.
        """
        self.assertRaises(TypeError, lambda: get_player_manager(TEST_PLAYERS_DAMAGED_FILE_PATH))
