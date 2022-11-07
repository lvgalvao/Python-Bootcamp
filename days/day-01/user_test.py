from faker import Faker
from user import User


def test_band_name():
    faker = Faker()
    citie = faker.city()
    name = faker.name()
    user = User(citie, name)
    assert user.band_name() == f"{citie} {name}"
