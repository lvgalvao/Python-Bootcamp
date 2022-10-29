import requests
from config import SHEETY_PRICES_ENDPOINT


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data


# just a comment
