import csv
from typing import List, Optional
import logging

from pydantic import BaseModel


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


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PlayerManager(metaclass=Singleton):
    players: List[Player]

    def __init__(self, file_path: str):
        try:
            with open(file_path, "r") as players_file:
                csv_reader = csv.DictReader(players_file)
                self.players = [Player(**raw_player) for raw_player in csv_reader]
        except FileNotFoundError as error:
            raise Exception("Players file not found, could not load players") from error

    def get_players(self) -> List[Player]:
        return self.players

    def get_player(self, player_id: str) -> Optional[Player]:
        try:
            requested_player = next(filter(lambda player: player_id == player.playerID, self.players))
        except StopIteration as error:
            logging.debug(f"Player with id:[{player_id}] was not found.", error)
            return None
        return requested_player


# In order to avoid reloading of the csv file, the player manager instance is created once.
def get_player_manager(file_path: str) -> PlayerManager:
    return PlayerManager(file_path=file_path)
