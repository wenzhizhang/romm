#!/usr/bin/env bash
# 把 names.zh.yml 里的中文名写入 RomM。改完映射文件后直接运行本脚本。
set -euo pipefail
cd "$(dirname "$0")"

docker cp names.zh.yml romm:/tmp/names.zh.yml

docker exec -i romm python - <<'PY'
import sys, yaml
sys.path.insert(0, '/backend')
from handler.database.base_handler import sync_session
from models.rom import Rom

mapping = yaml.safe_load(open('/tmp/names.zh.yml')) or {}
with sync_session() as s:
    by_fs = {r.fs_name: r for r in s.query(Rom).all()}
    changed = 0
    for fs_name, new_name in mapping.items():
        rom = by_fs.get(fs_name)
        if rom is None:
            print(f"跳过（库里没有这个文件）: {fs_name}")
            continue
        if not new_name or rom.name == new_name:
            continue
        print(f"{rom.id}: {rom.name} -> {new_name}")
        rom.name = new_name
        changed += 1
    s.commit()
print(f"更新 {changed} 条")
PY
