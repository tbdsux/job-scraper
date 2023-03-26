from typing import TypedDict


class SearchResult(TypedDict):
    title: str
    description: str
    link: str
    company: str
    location: str
    listed_date: str
    uid: str  # should have a custom id, usefull for other app projects to determine which has been seen already
