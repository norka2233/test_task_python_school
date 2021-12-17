import random


def generate_plate():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '0123456789'
    r = 2 * ''.join([c for c in random.choice(chars)]) + " " + ''.join(random.choice(nums)) + ''.join(random.choice(nums)) + ''.join(random.choice(nums)) + ''.join(random.choice(nums)) + " " + 2 * ''.join(random.choice(chars))
    return r
