from typing import Any, Dict

import requests
# import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from cloudscraper import create_scraper

default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def request(url: str, headers: Dict[str, Any] = {}) -> BeautifulSoup:
    r = requests.get(url, headers=default_headers | headers)

    if not r.ok:
        raise Exception("Request is not ok.")

    return BeautifulSoup(r.text, "lxml")


def c_request(url: str, headers: Dict[str, Any] = {}) -> BeautifulSoup:
    sess = requests.Session()
    sess.headers = default_headers | headers

    scraper = create_scraper(sess=sess)

    r = scraper.get(url)

    if not r.ok:
        raise Exception("Request is not ok.")

    return BeautifulSoup(r.text, "lxml")


# def u_request(url: str) -> BeautifulSoup:
#     options = uc.ChromeOptions()
#     options.headless = True

#     driver = uc.Chrome(
#         options=options, version_main=110  # my own version of chrome (TODO: update)
#     )

#     driver.get(url)
#     src = driver.page_source

#     return BeautifulSoup(src, "lxml")
