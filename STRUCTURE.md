# CURATOR STRUCTURE

One repo (`curator`). A single installable Python package in `src/curator/`, plus the target site and dashboard as FastAPI apps inside it.

## Create the project (Day 1)
```bash
uv init --package curator     # new project with src/ layout, pyproject.toml
cd curator
uv python pin 3.12            # fixes the Python version (.python-version)
uv sync                       # creates .venv and uv.lock from pyproject.toml
uv run python -c "print('ok')"  # runs a command inside the project environment
```
Add dependencies only when a day needs them: `uv add httpx` (adds to pyproject.toml and uv.lock). Dev tools: `uv add --dev pytest`.

## Layout
```
curator/
├── pyproject.toml            # NOW  deps + project metadata
├── uv.lock                   # NOW  exact versions (auto-generated, commit it)
├── .python-version           # NOW  pinned Python
├── .env.example              # NOW  names of env vars, no secrets
├── .gitignore                # NOW
├── README.md                 # NOW (stub), Week 8 (final)
├── docker-compose.yml        # Day 2  Redis + local Mongo (later: all services)
├── Dockerfile                # Week 8
├── tags.json                 # Week 4-5  ONE tag tree shared by the site and the LLM prompt
├── src/curator/
│   ├── config.py             # NOW  settings from env vars
│   ├── logging.py            # Week 7  structured logging
│   ├── db/                   # Day 2+  Mongo connection, article model, indexes
│   ├── adapters/             # Week 1-2  base.py (interface), devto.py, nasa.py
│   ├── nasa_spider/          # Week 2  Scrapy project (spider + item pipeline)
│   ├── queue/                # Week 3  Arq worker, job per stage, scheduler, retries
│   ├── stages/               # Week 2-6  plain functions per stage: scrape, generate, classify, upload
│   ├── generate/             # Week 4  PDF (fpdf2) and CSV builders
│   ├── llm/                  # Week 5  prompt builder, client, Pydantic schemas, eval script
│   ├── uploader/             # Week 6  Playwright upload + screenshots
│   ├── control/              # Week 7  kill switch flags, toggle log
│   ├── site/                 # Week 4  TARGET SITE: FastAPI app, templates/, static/
│   └── dashboard/            # Week 7  OPERATIONS DASHBOARD: FastAPI app, templates/, static/
├── data/                     # NOW (gitignored)  generated PDFs, CSVs, failure screenshots
├── evals/                    # Week 5  hand-labeled test set + results
├── docs/                     # Week 1+  weekly docs entries, architecture diagram
├── tests/                    # Week 1+  mirrors src/curator/
└── .github/workflows/        # Week 8  CI/CD
```

## Why things live where
- `adapters/` vs `stages/`: adapters only know how to read one source and return the normalized article. Stages are the pipeline steps that workers call.
- `queue/` holds only job wiring and retry settings; the real work stays in `stages/` so it can be tested without Redis.
- `site/` and `dashboard/` are separate FastAPI apps so the target site can be deployed alone.
- `tags.json` sits at the repo root because both the site and `llm/` read it.
- `data/` stays out of git; only file paths are stored in Mongo.
