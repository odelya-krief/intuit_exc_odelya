from typing import List, Optional

import uvicorn
from fastapi import FastAPI

from players import Player, PlayerManager

app = FastAPI()
player_manager = PlayerManager()


@app.get("/")
async def root():
    return "Intuit Home Exc."


@app.get("/api/players")
async def players() -> List[Player]:
    return player_manager.get_players()


@app.get("/api/players/{player_id}")
async def players(player_id: str) -> Optional[Player]:
    return player_manager.get_player(player_id=player_id)


# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8000)
