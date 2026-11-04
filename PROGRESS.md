# Progress

Commit after every class. Tag every Friday: `git tag week-N && git push origin week-N`.

## Week 1 (tag week-1 by Fri 23 Oct)
- [x] Repo created from the Examate template and registered on the form
- [x] README top section filled from my project card
- [x] /health runs locally
- [x] docs/QUESTIONS.md: 10 real questions
- [x] 50+ pages collected, DATASET.md filled, sample in data/sample/
- [x] Tag week-1 pushed

## Week 2 (tag week-2 by Fri 30 Oct)
- [x] POST /chat calls an LLM and returns structured JSON
- [x] Streaming, timeouts, retry and a fallback model
- [x] Cost log + GET /usage
- [x] Docker Compose (API + Postgres/pgvector) runs
- [x] CI green, live link in README
- [x] Tag week-2 pushed

## Week 3 (tag week-3 by Fri 6 Nov)
- [ ] Parser keeps page numbers and headings
- [ ] 500+ pages chunked, embedded and stored in pgvector
- [ ] POST /ask answers with [document, page] citations
- [ ] docs/EVAL_v0.md with my 10 questions scored
- [ ] Tag week-3 pushed

## Daily log
| **Date** | **What I did today** | **Commit** |
| -------- | -------------------- | ---------- |
| Nov 4, 2026 | Fixed Ruff formatting issues in the application files | `d9fba21` |
| Nov 4, 2026 | Added optional database URL setting to application configuration | `16c8ada` |
| Nov 4, 2026 | Updated database URL configuration | `91a9041` |
| Nov 4, 2026 | Added database URL configuration fix | `214b0eb` |
| Nov 4, 2026 | Added pre-commit hooks for code quality checks | `caf1c70` |
| Nov 4, 2026 | Configured pre-commit hooks | `85b5ab5` |
| Nov 4, 2026 | Added Docker smoke tests and automated test workflow | `a7db760` |
| Nov 4, 2026 | Configured Docker Compose with PostgreSQL and `/ready` health endpoint | `f69ada0` |