import requests
from config import SHEETY_PRICES_ENDPOINT


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def get_destionation_code(self):
        for city in self.destination_data:
            print(city)
            new_data = {
                "price": {
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",
                json=new_data
            )
            print(response.text)