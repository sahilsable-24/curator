# CURATOR PROGRESS (snapshot, max 40 lines, replaced fully each day)

## Status
- Current day: Day 2 done
- Week: 1
- Last session: Day 2 (docker-compose, Atlas, async Mongo + Redis hello world)
- Mood/pace: on track

## Completed (one line per finished week, compressed)
- (none yet)

## This week so far (max 7 lines)
- Day 1: uv project created, folders made, config.py (pydantic-settings) reads env vars, Docker hello-world works, repo pushed to GitHub
- Day 2: docker-compose.yml runs Redis 7 + Mongo 7 (named volume); Atlas M0 cluster connected; db/hello.py pings local Mongo, Atlas and Redis with async clients; fixed config.py by adding env_file=".env"

## Pipeline state (tick as working end to end)
- Tooling set up: uv yes / Docker yes / Mongo yes (local + Atlas) / Redis yes
- Dev.to adapter: no
- NASA spider: no
- Queue + workers: no
- PDF + CSV generation: no
- Classification: no
- Playwright upload: no
- Operations dashboard (runs, next schedule, kill switch): no

## Current state of the code
- Folders/files that exist: pyproject.toml, uv.lock, .python-version, .env.example, .gitignore, README.md, docker-compose.yml, src/curator/config.py, src/curator/db/ (__init__.py, hello.py throwaway), data/, docs/, tests/
- What works end to end: settings load from .env; async hello world against local Mongo, Atlas and Redis
- Env vars: MONGODB_URI (app's Mongo, local for now), MONGODB_URI_ATLAS (Atlas test), REDIS_URL, KILL_SWITCH_SECRET (unused until Week 7)

## Open problems / bugs (max 5)
- Atlas password was shared in chat on Day 2: rotate it and update .env (confirm done)
- Windows Git Bash: docker commands with -w /app or paths need MSYS_NO_PATHCONV=1

## Decisions made (max 8, most important only)
- uv for all Python packaging
- pydantic-settings for config (reused later for LLM validation)
- Local Mongo in Docker for dev, Atlas for deploy; same code, only MONGODB_URI changes
- PyMongo async client (AsyncMongoClient) for all DB access

## Next up
- Day 3: Design day 1: brand, product feel, color (light + dark), typography (DESIGN.md sections 0-3)

## Concepts I still feel shaky on
- (none yet)