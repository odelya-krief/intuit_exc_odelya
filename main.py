from typing import List, Optional

import uvicorn
from fastapi import FastAPI

import settings
from players import Player, get_player_manager

app = FastAPI()


def player_manager():
    return get_player_manager(file_path=settings.PLAYERS_FILE_PATH)


@app.get("/")
async def root():
    return "Intuit Home Exc."


@app.get("/api/players")
async def players() -> List[Player]:
    return player_manager().get_players()


@app.get("/api/players/{player_id}")
async def players(player_id: str) -> Optional[Player]:
    return player_manager().get_player(player_id=player_id)

