import datetime
import json
import re

from bs4 import BeautifulSoup

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}
DAYS = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7,
}


class ScrapeEngineHelper:
    @staticmethod
    def get_info_from_title(container):
        month_year_map = {}
        title = container.get("title").split(" ")
        for index, value in enumerate(title):
            if value.lower() in MONTHS:
                month_year_map[value.lower()] = int(title[index + 1])

        return month_year_map

    @staticmethod
    def get_days_from_li(container, month_year_map):
        output = []
        soup = BeautifulSoup(container.get("description"), "html.parser")
        for li in soup.select("li"):
            day, message = li.get_text().split(" – ")
            day_list = day.split(" ")

            counter = 0
            to_bool = False
            while counter < len(day_list):
                # if the word is a day of the week, then the next two
                # words should be the date and the month
                if day_list[counter].lower() in DAYS:
                    date, month = day_list[counter + 1], day_list[counter + 2]
                    if month == "and":
                        month = day_list[-1]

                    output_element = datetime.datetime(
                        month_year_map[month.lower()], MONTHS[month.lower()], int(date)
                    )
                    output.append(
                        (
                            output_element,
                            message,
                        )
                    )

                if day_list[counter].lower() == "to":
                    to_bool = True

                counter += 1

            if to_bool:
                start_date, end_date = output[-2][0], output[-1][0]
                while start_date + datetime.timedelta(days=1) < end_date:
                    start_date += datetime.timedelta(days=1)
                    output.append(
                        (
                            start_date,
                            message,
                        )
                    )

        return output

    @staticmethod
    def process_date(date_string, year):
        date = date_string.split(" ")
        month = MONTHS[date[-1].lower()]
        days = [i for i in date if i.isnumeric()]
        return [
            datetime.datetime(
                int(year),
                month,
                int(day),
            )
            for day in days
        ]

    @staticmethod
    def clean_and_get_dicts(element):
        res = re.findall(r"\[.*?]", element)
        dicts = re.findall(r"\{.*?}", res[0])
        return [json.loads(container.replace("'", '"')) for container in dicts]
