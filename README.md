# DisclosureDesk

## Problem
Listed companies need to disclose board meetings, financial results, related-party transactions and material events within strict SEBI deadlines. However, the relevant rules are spread across SEBI LODR Regulations, amendments, master circulars and later circulars. Finding the correct clause and deadline often requires checking multiple documents. Disclosure Desk helps company secretarial teams find the applicable requirements, deadlines and supporting clauses in one place.

## Who it is for
Assistant company secretaries and compliance teams at listed companies, especially mid-sized auto-components companies.

## Signature feature
Disclosure Clock: Shows the disclosure deadline for an event, along with the clause that specifies the time limit.

## Hardest problem (my interview story)
Cross-document comparison. A question such as “We are acquiring a 12% stake in a supplier. What must we disclose and by when?” may require information from multiple regulations, schedules and circulars. Disclosure Desk breaks the question into smaller sub-questions, retrieves the relevant information from each document and shows which source supports each part of the answer.

## Dataset
| Source | Link | Documents | Pages | Licence / terms |
|---|---|---|---|---|
| Securities and Exchange Board of India (SEBI) | https://www.sebi.gov.in/ | SEBI LODR Regulations, 2015, amendments, master circular and later LODR circulars | 900+ pages | Official SEBI publications; refer to the applicable document terms |

## 10 real questions
See [docs/QUESTIONS.md](docs/QUESTIONS.md).

## Run it
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env                                 # Windows: copy .env.example .env
uvicorn app.main:app --reload
curl localhost:8000/health
```

## Live link
<Added in Week 2>
