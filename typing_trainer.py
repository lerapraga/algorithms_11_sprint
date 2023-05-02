# 86829674

from collections import Counter
from typing import Tuple

NUMBER_OF_ROWS = 4
NUMBER_OF_PLAYERS = 2


def typing_trainer(k: int, digits: str) -> int:
    cnt = Counter(digits)
    new_cnt = [0 if value > k * NUMBER_OF_PLAYERS else 1 for value in cnt.values()]
    return sum(new_cnt)


def read_input() -> Tuple[int, str]:
    digits = []
    k = int(input())
    for i in range(4):
        digits.append(input())
    digits = "".join(digits)
    digits = "".join(c for c in digits if c.isdecimal())
    return (k, digits)


if __name__ == '__main__':
    k, digits = read_input()
    result = typing_trainer(k, digits)
    print(result)
