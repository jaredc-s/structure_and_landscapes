import random

random_generator = random.Random()


def mutate_value(value):
    if isinstance(value, int):
        return shift_by_one(value)
    else:
        raise TypeError("unknown type to mutate")


def shift_by_one(number):
    if random_generator.random() < 0.5:
        return number + 1
    else:
        return number - 1
