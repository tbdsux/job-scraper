from typing import List

from job_scraper.types import SearchResult
from job_scraper.utils import request

BASE_URL = "https://www.kalibrr.com"


class Kalibrr:
    def __init__(self) -> None:
        pass

    def search(self, query: str, page: int = 1):
        url = BASE_URL + f"/job-board/te/{query}/{page}"

        r = request(url)

        container = r.find("div", {"itemtype": "http://schema.org/ItemList"})
        all_results = container.find_all(
            "div", {"itemtype": "http://schema.org/ListItem"}
        )
        results: List[SearchResult] = []

        for i in all_results:
            raw_job = i.find("h2")

            job_title = raw_job.get_text().strip()
            job_link = BASE_URL + raw_job.find("a").get("href")

            raw_info = i.find(
                "div",
                class_="k-col-start-3 k-row-start-3 k-flex k-flex-col k-justify-end",
            )
            job_company = raw_info.find("span").get_text().strip()
            job_company_verified = (
                True
                if raw_info.find(attrs={"title": "verified-business"}) is not None
                else False
            )

            job_location = (
                raw_info.find("div", class_="k-flex k-flex-col md:k-flex-row")
                .find("a")
                .get_text()
                .strip()
            )

            job_listed_date = (
                i.find(
                    "div",
                    class_="k-col-start-5 k-row-start-1 k-text-right k-text-xs k-text-subdued k-hidden k-mb-2 md:k-block",
                )
                .find("span")
                .get_text()
                .strip()
            )

            results.append(
                {
                    "title": job_title,
                    "link": job_link,
                    "company": {"name": job_company, "verified": job_company_verified},
                    "listed_date": job_listed_date,
                    "location": job_location,
                }
            )

        return results
