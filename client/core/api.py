from fastapi import APIRouter
from . import hypcore

router = APIRouter()

@router.get("/get_all_games")
async def get_games(area: str = "国服", language: str = "zh-cn"):
    # TODO: Implement the logic to get games from the database
    return await hypcore.获取全部游戏(area, language)
