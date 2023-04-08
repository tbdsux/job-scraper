# job-scraper

Job Scraper for jobs from the Philippines from various job posting websites as a python library.

## Install

```sh
python3 -m pip install phjob-scraper
```

## Available websites

- **[Jora](https://ph.jora.com)**

  ```python
  from job_scraper import Jora

  src = Jora()
  results = src.search("quality assurance", location="manila")

  for i in results:
      print(i["title"])
  ```

- **[Indeed](https://ph.indeed.com)**

  Note: frequent usage within a few duration of time might raise CloudflareError from `cloudscraper`

  ```python
  from job_scraper import Indeed

  src = Indeed()

  results = src.search("developer", location="baguio")
  print(results)
  ```

##

**@tbdsux | &copy; 2023**
