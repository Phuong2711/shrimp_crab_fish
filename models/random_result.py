# -*- coding: utf-8 -*-
from random import randint

RESULT = {1: 's', 2: 'c', 3: 'f', 4: 'd', 5: 'g', 6: 'r'}
DICE_FACES = 6


def get_random_result(n):
    return [RESULT[randint(1, DICE_FACES)] for _ in range(n)]


if __name__ == "__main__":
    print(get_random_result(3))

