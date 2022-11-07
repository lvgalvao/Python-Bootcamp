class User:
    def __init__(self, city, pet_name):
        self.city = city
        self.pet_name = pet_name

    def band_name(self):
        return self.city + " " + self.pet_name
