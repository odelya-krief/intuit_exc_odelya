from typing import List, Optional
from fastapi import FastAPI

import settings
from players_manager.players import Player, get_player_manager

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)