from typing import List
from urllib.parse import quote

from job_scraper.types import SearchResult
from job_scraper.utils import c_request

BASE_URL = "https://ph.indeed.com/"


class Indeed:
    def __init__(self) -> None:
        pass

    def search(self, query: str, location: str, page: int = 1):
        url = BASE_URL + f"rss?q={quote(query)}&l={quote(location)}"
        if page != 1:
            url += f"&page={str(page + 1)}0"

        r = c_request(url, {}, "xml")

        items = r.find_all("item")
        results: List[SearchResult] = []

        for item in items:
            raw_job_title = item.find("title").get_text().split("-")

            job_title = raw_job_title[0].strip()
            job_id = item.find("guid").get_text().strip()
            job_company = raw_job_title[1].strip()
            job_location = raw_job_title[2].strip()
            raw_job_description = item.find("description").get_text().split("<br>")
            job_description = raw_job_description[0].strip()
            job_listed_date = item.find("pubDate").get_text()
            job_link = item.find("link").get_text()

            results.append(
                {
                    "uid": job_id,
                    "company": job_company,
                    "title": job_title,
                    "description": job_description,
                    "link": job_link,
                    "listed_date": job_listed_date,
                    "location": job_location,
                }
            )

        return results
