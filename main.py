from typing import List, Optional
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

"""
    If I had infinite time:
    1. Add integration tests, creating HTTP requests to the server, and asserting on the results.
    2. Add dummy unit tests for the Fast API server. (To make sure things will not break in the future.)
    3. Currently the /api/players endpoint is not working on Vercel, because the amount of data an AWS
       lambda can return is limited, so if I had time I would add pagination or some sort 
       of chunking of the data.
    4. CSV is a fragile, not secure and not scalable format, storing the data in a database 
       will be a lot better, in terms of security, future updates and changes, scale, speed, tests
       and deployment. 
    5. Add a better configuration management.
"""
