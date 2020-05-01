import requests


class PageRequester:
    def __init__(self, url: str):
        self._url = url

    def get(self) -> str:
        return requests.get(self._url).text
