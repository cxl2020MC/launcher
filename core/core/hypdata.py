from pathlib import Path
from . import hypcore

import json

data_dir = Path("./data/")
data_dir.mkdir(exist_ok=True)

async def 更新游戏缓存():
    data = await hypcore.获取全部游戏("国服")
    with open(data_dir / "games.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

