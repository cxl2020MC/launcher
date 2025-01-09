import asyncio
from core import hypcore
import json
# print(asyncio.run(获取游戏配置("国服", "1Z8W5NHUQb")))
# x6znKlJ0xK
# print(asyncio.run(获取游戏配置("国服", "1Z8W5NHUQb")))
data = asyncio.run(hypcore.获取游戏内容("国际服", "nap_cn"))
# print(data)
print(json.dumps(data, indent=4, ensure_ascii=False))
