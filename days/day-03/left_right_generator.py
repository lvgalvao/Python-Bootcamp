from random import randint


class RandomMovement:
    def left_or_right(self):
        direcionamento = "right"
        if randint(0, 1) == 1:
            direcionamento = "left"
        return direcionamento
