import json
import re

import requests
from bs4 import BeautifulSoup


class ScrapeEngine:
    url = "https://www.networkrail.co.uk/industrial-action/"

    payload = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    def run_get_request(self) -> requests.Response:
        return requests.request("GET", self.url, headers=self.headers, data=self.payload)

    @staticmethod
    def clean_and_get_dicts(element):
        res = re.findall(r"\[.*?]", element)
        dicts = re.findall(r"\{.*?}", res[0])
        return [
            json.loads(container.replace("'", "\"")) for container in dicts
        ]

    @staticmethod
    def print_response(dicts):
        for container in dicts:
            print(container.get("title"))
            html_list = BeautifulSoup(container.get("description"), "html.parser")
            for li in html_list.select("li"):
                print(li.get_text())

    def get_list_elements(self):
        response = self.run_get_request()
        soup = BeautifulSoup(response.text, "html.parser")

        for accordion in soup.select("accordion"):
            element = accordion.find_next().find_next().attrs.get("v-for")
            dicts = self.clean_and_get_dicts(element)
            self.print_response(dicts)
