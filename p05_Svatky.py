# https://svatky.adresa.info/json?date=2502
import requests


class NameDays:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_name(self, date):
        #response = requests.get("https://svatky.adresa.info/json?date=2502")
        response = requests.get(f"{self.api_url}json?date={date}")
        data = response.json()[0]
        return data["name"]


if __name__ == '__main__':
    name_days = NameDays("https://svatky.adresa.info/")
    dates = ["0102", "2002", "3004", "0205"]
    for date in dates:
        print(f"{date}: {name_days.get_name(date)}")
