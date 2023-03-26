from typing import List
from urllib.parse import quote

from job_scraper.types import SearchResult
from job_scraper.utils import c_request

BASE_URL = "https://ph.jora.com"


class Jora:
    def __init__(self) -> None:
        pass

    def search(self, query: str, location: str, page: int = 1):
        url = BASE_URL + f"/j?q={quote(query)}&l={quote(location)}&st=date&p={page}"

        r = c_request(url)

        container = r.find("div", id="jobresults")
        all_results = container.find_all("article", class_="job-card")
        results: List[SearchResult] = []

        for i in all_results:
            raw_job_link = i.find("a", class_="job-link")

            job_title = raw_job_link.get_text().strip()
            job_id = i.get("id")
            job_link = BASE_URL + raw_job_link.get("href")
            job_company = i.find("span", class_="job-company").get_text().strip()
            job_location = i.find("a", class_="job-location").get("href")
            job_description = i.find("div", class_="job-abstract").get_text().strip()

            try:
                job_listed_date = (
                    i.find("span", class_="job-listed-date").get_text().strip()
                )
            except Exception:
                job_listed_date = ""

            results.append(
                {
                    "uid": job_id,
                    "title": job_title,
                    "company": job_company,
                    "description": job_description,
                    "link": job_link,
                    "location": job_location,
                    "listed_date": job_listed_date,
                }
            )

        return results
