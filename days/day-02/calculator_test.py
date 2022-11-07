from calculator import Calculator
from test.tip import TipSpy
from faker import Faker

fake = Faker()

total = fake.random_number()
person = fake.random_number()
porcentager = fake.random_number()


def test_tip_calculator():
    tip = TipSpy()
    calculator = Calculator(tip)
    result = calculator.tip_calculator(total, person, porcentager, True)

    # input tests
    assert tip.tip_attributer["total_bill"] == total
    assert tip.tip_attributer["people_to_split"] == person
    assert tip.tip_attributer["percentage"] == porcentager

    # output test
    assert result is not None
