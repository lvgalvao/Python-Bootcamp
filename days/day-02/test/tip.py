from faker import Faker

fake = Faker()


class TipSpy:
    def __init__(self):
        self.tip_attributer = {}

    def tip_calculator(self, total_bill, people_to_split, percentage):
        self.tip_attributer["total_bill"] = total_bill
        self.tip_attributer["people_to_split"] = people_to_split
        self.tip_attributer["percentage"] = percentage

        return fake.random_number()
