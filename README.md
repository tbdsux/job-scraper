# job-scraper

Job Scraper for jobs from the Philippines from various job posting websites as a python library.

## Available websites

- **[Jora](https://ph.jora.com)**

  ```python
  from job_scraper import Jora

  src = Jora()
  results = src.search("quality assurance", location="manila")

  for i in results:
      print(i["title"])
  ```
