import csv
from typing import List, Optional
import logging

from pydantic import BaseModel

PLAYERS_FILE_NAME = "player.csv"


class Player(BaseModel):
    playerID: str
    birthYear: str
    birthMonth: str
    birthDay: str
    birthCountry: str
    birthState: str
    birthCity: str
    deathYear: str
    deathMonth: str
    deathDay: str
    deathCountry: str
    deathState: str
    deathCity: str
    nameFirst: str
    nameLast: str
    nameGiven: str
    weight: str
    height: str
    bats: str
    throws: str
    debut: str
    finalGame: str
    retroID: str
    bbrefID: str


class PlayerManager:
    players: List[Player]

    def __init__(self):
        try:
            with open("player.csv", "r") as players_file:
                self.players = [Player(**raw_player) for raw_player in csv.DictReader(players_file)]
        except FileNotFoundError as error:
            logging.error("Players file not found,couldn't load players", error)
            raise error

    def get_players(self) -> List[Player]:
        return self.players

    def get_player(self, player_id: str) -> Optional[Player]:
        try:
            requested_player = next(filter(lambda player: player_id == player.playerID, self.players))
        except StopIteration as error:
            logging.debug(f"Player with id:[{player_id}] was not found.", error)
            return None
        return requested_player
