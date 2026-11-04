"""
Scrapes direct PDF links from SEBI listing & regulation pages.
Usage:
    python tools/find_sebi_pdfs.py --out urls.txt
    python tools/find_sebi_pdfs.py --filter "listing obligations" --out urls.txt
"""

import argparse
import re
import time

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "ExamateStudentProject/1.0 (learning project; contact: mabhusubhani001@gmail.com)"}
DELAY = 1.5  # Polite delay between page requests

MASTER_CIRCULARS_URL = "https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=1&ssid=6&smid=0"
LODR_REGULATION_PAGE = (
    "https://www.sebi.gov.in/legal/regulations/jan-2026/"
    "securities-and-exchange-board-of-india-listing-obligations-and-disclosure-requirements-"
    "regulations-2015-last-amended-on-january-22-2026-_99375.html"
)


def get_pdf_from_article(article_url: str) -> str | None:
    """Visits a SEBI article page and extracts the direct PDF URL from its iframe."""
    try:
        resp = requests.get(article_url, headers=HEADERS, timeout=20)
        if resp.status_code != 200:
            return None
        # Match PDF inside iframe: sebi_data/attachdocs/...pdf
        match = re.search(
            r"https://www.sebi.gov.in/sebi_data/attachdocs/[^\'\"\s]+\.pdf",
            resp.text,
        )
        if match:
            return match.group(0)
    except Exception as e:
        print(f"Error fetching {article_url}: {e}")
    return None


def scrape_sebi_master_circulars(keyword_filter: str | None = None) -> list[tuple[str, str, str]]:
    """Fetches Master Circulars listing and returns (title, date, pdf_url)."""
    print(f"Fetching Master Circulars listing from {MASTER_CIRCULARS_URL}...")
    resp = requests.get(MASTER_CIRCULARS_URL, headers=HEADERS, timeout=20)
    if resp.status_code != 200:
        print(f"Failed to fetch listing: {resp.status_code}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.select("table#sample_1 tbody tr")
    results = []

    for row in rows:
        tds = row.find_all("td")
        if len(tds) < 2:
            continue
        date_str = tds[0].get_text(strip=True)
        link_tag = tds[1].find("a")
        if not link_tag or not link_tag.get("href"):
            continue

        title = link_tag.get_text(strip=True)
        article_url = link_tag["href"].strip()

        # Apply optional filter (e.g., 'lodr' or 'listing obligations')
        if keyword_filter and keyword_filter.lower() not in title.lower():
            continue

        print(f"Found: [{date_str}] {title}")
        time.sleep(DELAY)
        pdf_url = get_pdf_from_article(article_url)
        if pdf_url:
            print(f"  -> PDF: {pdf_url}")
            results.append((title, date_str, pdf_url))
        else:
            print("  -> No PDF found in iframe")

    return results


def main():
    parser = argparse.ArgumentParser(description="Find direct SEBI PDF links.")
    parser.add_argument("--out", default="urls.txt", help="Output file to append/write URLs")
    parser.add_argument("--filter", default=None, help="Optional keyword filter on title")
    parser.add_argument("--all-master", action="store_true", help="Fetch all master circulars on page 1")
    args = parser.parse_args()

    found_entries = []

    # 1. First get the core LODR Regulation document itself
    print("Checking LODR Regulation page...")
    lodr_pdf = get_pdf_from_article(LODR_REGULATION_PAGE)
    if lodr_pdf:
        found_entries.append(
            (
                "SEBI (Listing Obligations and Disclosure Requirements) Regulations 2015 [Amended Jan 2026]",
                "Jan 22, 2026",
                lodr_pdf,
            )
        )

    # 2. Scrape Master Circulars (either filtered by LODR or all on page 1)
    kw = args.filter if args.filter else (None if args.all_master else "listing obligations")
    circular_entries = scrape_sebi_master_circulars(keyword_filter=kw)
    found_entries.extend(circular_entries)

    # 3. Write results to output file
    with open(args.out, "w", encoding="utf-8") as f:
        for title, date_str, pdf_url in found_entries:
            f.write(f"# {date_str} - {title}\n")
            f.write(f"{pdf_url}\n\n")

    print(f"\nDone! Saved {len(found_entries)} direct PDF links to {args.out}")


if __name__ == "__main__":
    main()
