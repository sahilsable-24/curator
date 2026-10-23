# PROJECT: Curator

## What I'm building
Curator is an automation pipeline. It scrapes articles from two sources, generates one PDF per article plus a CSV of metadata, classifies each article against a tag tree (tags with sub-tags, multiple tags per article) using an LLM, and uploads everything to a target website through its upload form. Every step is queued, retried safely and tracked.

Suggested URLs: curator-target (the target site), GitHub repo: curator

## The pipeline
1. Scrape: NASA articles (HTML, Scrapy spider) and Dev.to articles (API, httpx). Each source has an adapter returning the same normalized article: title, author, date, topic, body, source URL.
2. Dedupe: unique index on URL + content hash in MongoDB.
3. Generate: one PDF per article + a CSV (name, date, topic, author, PDF filename).
4. Classify: LLM picks tags and sub-tags from the tag tree (structured output, validated in code, confidence score). Low confidence goes to a review list.
5. Upload: Playwright fills the target site's form: attach PDF, tick tags and sub-tags, fill source URL. Screenshot on failure, verify success.
6. Track: every article has a status (scraped, generated, classified, uploaded, failed) and a retry count.

## Target site (I build it myself, simple but good-looking)
FastAPI app with an upload page: PDF upload, tag + sub-tag picker, source URL field. Plus a list of uploaded articles. No login. The tag tree lives in one shared file (tags.json) used by the site and the LLM prompt.

## Operations dashboard (observability + control)
One page to see and control the whole pipeline:
- Overview: articles per stage, failures, retries, LLM cost/usage
- Scrape runs: history per source (start/end time, duration, articles found, new vs duplicate, errors)
- Schedule: next scheduled run per source, with a countdown
- Kill switch: pause/resume the whole pipeline or a single source. Graceful by default (workers finish the current job, take no new ones), checked by workers before every job. Every toggle is logged (who/when/why).
- Optional: "run now" button per source
The pipeline flow itself does not change; the dashboard only observes it and flips flags.
No login for Curator, but kill switch and run-now endpoints are protected by a simple shared secret (env variable) so a public deployment can't be paused by strangers.

## Stack
- Language: Python, managed with uv (pyproject.toml, uv.lock; no pip or requirements.txt)
- Scraping: Scrapy (NASA, HTML), httpx (Dev.to, API)
- Upload automation: Playwright
- Storage: MongoDB Atlas free tier (PyMongo async). PDFs on disk/object storage, only the path in the DB
- Queue/coordination: Redis (queue, locks, rate limits) with Celery or Arq (decide early, with tradeoffs)
- LLM: Gemini or Groq free tier, Pydantic for validating structured output
- PDF: a simple Python PDF library (Claude to recommend the easiest)
- Target site + dashboard: FastAPI + Jinja templates + Tailwind
- Docker for local dev, GitHub Actions for CI/CD
- Deploy on free tiers where realistic (Playwright is heavy; Claude advises what runs where)
- No paid services (maybe a domain at the very end). No login or roles (only a shared secret on the kill switch endpoints).

## Concepts to learn (rough order)
1. Source adapters: one interface, two very different sources (HTML vs API)
2. Scraping basics: Scrapy spiders, item pipelines, throttling, robots.txt, politeness
3. MongoDB: document design, unique indexes, atomic status updates
4. Queues and workers: Redis, separate jobs per stage, scheduling
5. Idempotency and dedupe: retries never create duplicates
6. Retries with backoff, dead-letter handling, failure states
7. File generation: PDF per article, CSV export
8. LLM classification: structured output, Pydantic validation, hierarchical multi-label tags, confidence, review list
9. Browser automation: Playwright upload, selectors, waits, screenshots, verifying success
10. Observability and control: structured logging, run history, metrics, alerts when a scraper breaks, operations dashboard, cost tracking, kill switch (feature flag in Redis/Mongo checked by workers), reading the scheduler's next run time
11. Evals: hand-labeled test set, accuracy numbers
12. Production: tests, Docker, CI/CD, deployment, volume test (backfill thousands of NASA articles)
13. Stretch (only if time): LLM fallback extraction when a page layout changes; wrap the pipeline tools as an MCP server

## My situation
- Intermediate programmer, working alone
- 1 hour per day, 8 weeks (~56 sessions)
- Free Claude plan, so token efficiency matters

## Weekly shape (high level)
- Week 1: setup (uv, Docker, Mongo, Redis), design decisions for target site, data model, adapter interface, Dev.to adapter
- Week 2: NASA Scrapy spider, pipeline into Mongo, dedupe
- Week 3: queue, workers, scheduler, retries, status flow
- Week 4: PDF + CSV generation, build the target site with its design
- Week 5: LLM classification, tag tree, validation, review list
- Week 6: Playwright upload automation, idempotent uploads, failure handling
- Week 7: operations dashboard (runs, next schedule, kill switch), observability, evals with labeled set, stretch items
- Week 8: Docker, CI/CD, deployment, volume test, README + architecture diagram

(Detailed day-by-day plan lives in ROADMAP.md.)
