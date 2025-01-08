import aiohttp
import asyncio
import httpx


def get_hyp_api_url(区服: str, api: str, language: str = "zh-cn") -> str:
    if 区服 == '国服':
        host = "hyp-api.mihoyo.com"
    elif 区服 == '国际服':
        host = "sg-hyp-api.hoyolab.com"
    else:
        raise Exception("不支持的启动器")
    url = f"https://{host}/hyp/hyp-connect/api/{api}"
    return url


def get_launcher_id(区服: str) -> str:
    if 区服 == '国服':
        return "jGHBHlcOq1"
    elif 区服 == '国际服':
        return "VYTpXlbWo8"
    else:
        raise Exception("不支持的启动器")


def get_hyp_api_params(区服: str = "国服", language: str = "zh-cn") -> dict:
    return {
        "launcher_id": get_launcher_id(区服),
        "language": language
    }


async def get_game_id(游戏: str) -> str:
    if 游戏 == "原神":
        return "1Z8W5NHUQb"
    elif 游戏 == "绝区零":
        return "x6znKlJ0xK"
    elif 游戏 == "崩坏星穹铁道":
        return "64kMb5iAWu"
    elif 游戏 == "崩坏3":
        return "osvnlOc0S8"
    else:
        raise Exception("不支持的游戏")


# https://hyp-api.mihoyo.com/hyp/hyp-connect/api/getGameContent?launcher_id=jGHBHlcOq1&game_id=1Z8W5NHUQb&language=zh-cn
async def 获取资讯(区服, game_id: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGameContent", language) + \
        f"&game_id={game_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取全部游戏(区服, language="zh-cn"):
    url = get_hyp_api_url(区服, "getGames", language)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取全部游戏基本信息(区服, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getAllGameBasicInfo", language)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取游戏(区服, game_id: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGames", language) + f"&game_id={game_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取游戏基本信息(区服, game_id: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getAllGameBasicInfo",
                          language) + f"&game_id={game_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取全部游戏安装包信息(区服, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGamePackages", language)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取游戏安装包信息(区服, game_id: str, language="zh-cn") -> dict | None:
    ret_data = await 获取全部游戏安装包信息(区服, language)
    for i in ret_data["data"]["game_packages"]:
        if i["game"]["id"] == game_id:
            return i

# 暂时不可用


async def 获取多个游戏安装包信息(区服, game_ids: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGamePackages", language) + \
        f"&game_ids[]={game_ids}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def 获取游戏依赖(区服, game_id: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGameDeprecatedFileConfigs",
                          language) + f"&game_id={game_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


# 游戏配置
async def 获取游戏配置(区服, game_id: str, language="zh-cn") -> dict:
    url = get_hyp_api_url(区服, "getGameConfigs", language) + \
        f"&game_id={game_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


if __name__ == "__main__":
    # print(asyncio.run(获取游戏配置("国服", "1Z8W5NHUQb")))
    # x6znKlJ0xK
    # print(asyncio.run(获取游戏配置("国服", "1Z8W5NHUQb")))
    print(asyncio.run(获取多个游戏安装包信息("国服", "x6znKlJ0xK")))
