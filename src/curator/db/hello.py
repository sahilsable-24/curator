import asyncio

import redis.asyncio as aioredis
from pymongo import AsyncMongoClient

from curator.config import settings

async def check_mongo(label:str, url:str) -> None:
    """Connect to a mongo server, write one document, read it back"""

    client = AsyncMongoClient(url)

    try:
        await client.admin.command("ping")
        print(f"[{label}] ping ok")

        collection = client["hello_test"]["items"]
        await collection.insert_one({"msg": f"hello from {label}"})

        doc = await collection.find_one({"msg": f"hello from {label}"})
        print(f"[{label}] read back: {doc}")


        await collection.delete_many({})

    finally:
        await client.close()


async def check_redis() -> None:
    r = aioredis.from_url(settings.redis_url)

    try:
        print("[redis] ping:", await r.ping())
        await r.set("hello", "world")
        print("[redis] get:", await r.get("hello"))
    finally:
        await r.aclose()


async def main() -> None:
    await check_mongo("local", settings.mongodb_uri)
    if settings.mongodb_uri_atlas:
        await check_mongo("atlas", settings.mongodb_uri_atlas)
    await check_redis()


if __name__ == "__main__":
    asyncio.run(main())