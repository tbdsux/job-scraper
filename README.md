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

##

**@tbdsux | &copy; 2023**
