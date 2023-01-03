import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from db.strikes import Strikes
from db.utils import EngineFactory
from strike_scraper.scrape_engine_helpers import ScrapeEngineHelper


class ScrapeEngine(ScrapeEngineHelper):
    url = "https://www.networkrail.co.uk/industrial-action/"

    payload = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
    }

    def run_get_request(self) -> requests.Response:
        return requests.request(
            "GET", self.url, headers=self.headers, data=self.payload
        )

    def get_list_elements(self):
        response = self.run_get_request()
        soup = BeautifulSoup(response.text, "html.parser")

        for accordion in soup.select("accordion"):
            element = accordion.find_next().find_next().attrs.get("v-for")
            dicts = self.clean_and_get_dicts(element)
            month_year_map = self.get_info_from_title(dicts[0])
            days = self.get_days_from_li(dicts[0], month_year_map)
            self.upload_strike_dates_to_database(days)

    @staticmethod
    def upload_strike_dates_to_database(days):
        engine = EngineFactory(echo=False).create_from_config("../secrets/.local.env")
        with Session(engine) as session:
            for day, message in days:
                query = session.query(Strikes).filter(Strikes.date_of_strike == day)
                if query.count():
                    continue

                new_strike = Strikes(
                    date_of_strike=day,
                    strike_message=message,
                )
                session.add(new_strike)
                session.commit()


if __name__ == "__main__":
    scrape_engine = ScrapeEngine()
    scrape_engine.get_list_elements()
