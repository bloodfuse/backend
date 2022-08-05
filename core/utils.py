from string import ascii_letters, digits
from random import choices, seed
from time import time


seed = time()


def get_random_string(count: int):
    return ''.join(choices(ascii_letters + digits, k=count))


if __name__ == '__main__':
    count = 5
    rand = get_random_string(count)
    print(rand)
