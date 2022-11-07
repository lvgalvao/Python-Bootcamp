class Tip:
    def tip_calculator(self, total_bill, people_to_split, percentage):
        return total_bill * (1 + percentage) / people_to_split
