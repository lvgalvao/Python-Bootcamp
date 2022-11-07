from tip import Tip
from faker import Faker

faker = Faker()
total = faker.random_number()
person = faker.random_number()
porcentager = faker.random_number()


def test_tip_calculator():
    tip = Tip()
    result = tip.tip_calculator(total, person, porcentager)
    expect = (total * (1 + porcentager)) / person
    assert result == expect
