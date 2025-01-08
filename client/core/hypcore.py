# import aiohttp
import asyncio
import httpx
import json
from pathlib import Path


client = httpx.AsyncClient()


def get_hyp_api_url(区服: str, api: str) -> str:
    if 区服 == "国服":
        host = "hyp-api.mihoyo.com"
    elif 区服 == "国际服":
        host = "sg-hyp-api.hoyolab.com"
    else:
        raise Exception("不支持的启动器")
    url = f"https://{host}/hyp/hyp-connect/api/{api}"
    return url


def get_launcher_id(区服: str) -> str:
    if 区服 == "国服":
        return "jGHBHlcOq1"
    elif 区服 == "国际服":
        return "VYTpXlbWo8"
    elif 区服 == "B服原神":
        return "umfgRO5gh5"
    elif 区服 == "B服星铁":
        return "6P5gHMNyK3"
    elif 区服 == "B服绝区零":
        return "xV0f4r1GT0"
    else:
        raise Exception("不支持的启动器")


async def get_game_id(区服: str, game: str) -> str:
    # if game == "原神":
    #     return "1Z8W5NHUQb"
    # elif game == "绝区零":
    #     return "x6znKlJ0xK"
    # elif game == "崩坏星穹铁道":
    #     return "64kMb5iAWu"
    # elif game == "崩坏3":
    #     return "osvnlOc0S8"
    # else:
    #     raise Exception("不支持的游戏")
    data = await 获取全部游戏(区服)
    for i in data["data"]["games"]:
        if i["biz"] == game:
            return i["id"]
    raise Exception("不支持的游戏")




def get_hyp_api_params(区服: str = "国服", language: str = "zh-cn") -> dict:
    return {
        "launcher_id": get_launcher_id(区服),
        "language": language,
        # "game_id": get_game_id(游戏)
    }


# https://hyp-api.mihoyo.com/hyp/hyp-connect/api/getGameContent?launcher_id=jGHBHlcOq1&game_id=1Z8W5NHUQb&language=zh-cn
async def 获取游戏内容(区服, game: str, language: str = "zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGameContent")
    params = get_hyp_api_params(区服, language)
    params["game_id"] = await get_game_id(区服, game)
    resp = await client.get(url, params=params)
    return resp.json()


async def 获取全部游戏(区服, language="zh-cn"):
    url = get_hyp_api_url(区服, "getGames")
    resp = await client.get(url, params=get_hyp_api_params(区服, language))
    return resp.json()


async def 获取全部游戏基本信息(区服, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getAllGameBasicInfo")
    resp = await client.get(url, params=get_hyp_api_params(区服, language))
    return resp.json()


async def 获取游戏(区服, game: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGames")
    params = get_hyp_api_params(区服, language)
    params["game_id"] = await get_game_id(区服, game)
    resp = await client.get(url, params=params)
    return resp.json()


async def 获取游戏基本信息(区服, game: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getAllGameBasicInfo")
    params = get_hyp_api_params(区服, language)
    params["game_id"] = await get_game_id(区服, game)
    resp = await client.get(url, params=params)
    return resp.json()


async def 获取全部游戏安装包信息(区服, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGamePackages")
    resp = await client.get(url, params=get_hyp_api_params(区服, language))
    return resp.json()


async def 获取游戏安装包信息(区服, game: str, language="zh-cn") -> dict | None:
    ret_data = await 获取全部游戏安装包信息(区服, language)
    game_id = await get_game_id(区服, game)
    for i in ret_data["data"]["game_packages"]:
        if i["game"]["id"] == game_id:
            return i


async def 获取多个游戏安装包信息(区服, game_ids: list[str], language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGamePackages")
    params = get_hyp_api_params(区服, language)
    params["game_ids"] = game_ids
    resp = await client.get(url, params=params)
    return resp.json()


async def 获取游戏依赖(区服, game: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(
        区服, "getGameDeprecatedFileConfigs")
    params = get_hyp_api_params(区服, language)
    params["game_id"] = game
    resp = await client.get(url, params=params)
    return resp.json()

async def 获取游戏配置(区服, game: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGameConfigs")
    params = get_hyp_api_params(区服, language)
    params["game_id"] = game
    resp = await client.get(url, params=params)
    return resp.json()


if __name__ == "__main__":
    import json
    # print(asyncio.run(获取游戏配置("国服", "1Z8W5NHUQb")))
    # x6znKlJ0xK
    # print(asyncio.run(获取游戏配置("国服", "1Z8W5NHUQb")))
    data = asyncio.run(获取游戏安装包信息("国服", "nap_cn"))
    # print(data)
    print(json.dumps(data, indent=4, ensure_ascii=False))