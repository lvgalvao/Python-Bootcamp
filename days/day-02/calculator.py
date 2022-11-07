class Calculator:
    def __init__(self, tip):
        self.tip = tip

    def tip_calculator(self, total_bill, people_to_split, percentage, op):
        if op:
            return self.tip.tip_calculator(total_bill, people_to_split, percentage)
        return None
