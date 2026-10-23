# CURATOR ROADMAP (8 weeks, 56 days, ~1 hour/day)

Every 7th day is a lighter review/catch-up day. UI code starts only after DESIGN.md is fully filled (Day 4).

## Weekly goals
| Week | Goal |
|---|---|
| 1 | Tooling (uv, Docker, Mongo, Redis), design decisions, data model, adapter interface, Dev.to adapter |
| 2 | NASA Scrapy spider, items into Mongo, dedupe, politeness |
| 3 | Redis queue (Arq), workers per stage, scheduler, retries, status flow |
| 4 | PDF + CSV generation, build the target site with its design |
| 5 | LLM classification, tag tree, validation, review list, labeled eval set |
| 6 | Playwright upload, verification, idempotent uploads, failure handling |
| 7 | Operations dashboard (overview, runs, schedule, kill switch), observability, evals |
| 8 | Docker, CI/CD, deployment, volume test, README + architecture diagram |

## Day by day

### Week 1: Foundations and design
| Day | Focus |
|---|---|
| 1 | Create uv project, repo, folders, .env.example; run Python in Docker |
| 2 | docker-compose with Redis + local Mongo; connect to Atlas; PyMongo async hello world |
| 3 | Design day 1: brand, product feel, color (light + dark), typography (DESIGN.md sections 0-3) |
| 4 | Design day 2: tokens, wireframes for all key screens, tag picker + dashboard notes (sections 4-8). Design done. |
| 5 | Data model (article document, status, retry count) and the adapter interface (normalized article) |
| 6 | Dev.to adapter with httpx: fetch, normalize, rate limit, User-Agent |
| 7 | REVIEW: tests for the adapter, tidy, weekly docs entry |

### Week 2: Scraping and storage
| Day | Focus |
|---|---|
| 8 | Scrapy basics, robots.txt, politeness; NASA spider lists article URLs |
| 9 | NASA spider parses article pages into the normalized shape |
| 10 | Scrapy item pipeline writes to Mongo through the NASA adapter |
| 11 | Dedupe: unique index on URL + content hash, upserts |
| 12 | Throttling, caching fetched pages, handling bad pages |
| 13 | Atomic status updates in Mongo; run both sources end to end into the DB |
| 14 | REVIEW: tests, catch-up, weekly docs entry |

### Week 3: Queues, workers, scheduling
| Day | Focus |
|---|---|
| 15 | Redis + Arq hello world: enqueue, worker, result |
| 16 | One job per stage; status flow scraped to generated to classified to uploaded |
| 17 | Scrape jobs run through the worker for both sources |
| 18 | Retries with backoff; what is safe to retry |
| 19 | Dead-letter handling and failed state; manual retry of failed articles |
| 20 | Scheduler: cron per source, reading the next run time |
| 21 | REVIEW: kill and restart workers mid-job, confirm nothing duplicates; weekly docs entry |

### Week 4: Files and target site
| Day | Focus |
|---|---|
| 22 | PDF per article with fpdf2 |
| 23 | CSV export (name, date, topic, author, PDF filename) |
| 24 | Generate job: idempotent, file paths stored in Mongo, not the files |
| 25 | Target site skeleton: FastAPI, Jinja, Tailwind configured with design tokens |
| 26 | Upload page: PDF drop zone, tag + sub-tag picker reading tags.json, source URL field |
| 27 | Success/error states, uploaded articles list, loading/empty/error states, mobile check |
| 28 | REVIEW: polish against the anti "AI-look" checklist; weekly docs entry |

### Week 5: LLM classification
| Day | Focus |
|---|---|
| 29 | Finalize tags.json; LLM basics and why structured output |
| 30 | First Gemini/Groq call with structured output and a prompt built from tags.json |
| 31 | Pydantic validation against the tag tree; reject invented tags |
| 32 | Confidence score, threshold, low-confidence items to a review list |
| 33 | Classify job in the pipeline, with retries and token/cost recording |
| 34 | Hand-label a test set; write the eval script |
| 35 | REVIEW: first accuracy numbers, prompt tweaks; weekly docs entry |

### Week 6: Playwright upload
| Day | Focus |
|---|---|
| 36 | Playwright basics: selectors, waits, running against the target site |
| 37 | Fill the form: attach PDF, tick tags and sub-tags, source URL |
| 38 | Verify success; screenshot on failure |
| 39 | Idempotent uploads: never upload the same article twice |
| 40 | Upload job with retries and failure states |
| 41 | Full pipeline end to end on a small batch |
| 42 | REVIEW: break things on purpose (site down, bad selector) and check recovery; weekly docs entry |

### Week 7: Operations dashboard and observability
| Day | Focus |
|---|---|
| 43 | Structured logging; run records per source (start/end, found, new vs duplicate, errors) |
| 44 | Dashboard overview: articles per stage, failures, retries, LLM cost |
| 45 | Scrape runs table + run detail |
| 46 | Schedule panel with next-run countdown; review list page |
| 47 | Kill switch backend: flags in Redis/Mongo, workers check before every job, toggle log, shared-secret protection |
| 48 | Kill switch UI: paused vs running obvious at a glance, confirmation before pausing; optional run-now |
| 49 | REVIEW: scraper-broke alert, final eval numbers; weekly docs entry |

### Week 8: Production
| Day | Focus |
|---|---|
| 50 | Dockerfiles with uv; full docker-compose |
| 51 | Tests cleanup; GitHub Actions CI |
| 52 | Deploy target site + dashboard on a free tier |
| 53 | Decide and deploy what runs where (Playwright is heavy); CD |
| 54 | Volume test: backfill thousands of NASA articles, watch queues and failures |
| 55 | README + architecture diagram |
| 56 | REVIEW: interview walkthrough practice; stretch items only if time (LLM fallback extraction, MCP server) |
