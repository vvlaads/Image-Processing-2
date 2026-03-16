from enum import Enum


class WeightType(Enum):
    BALANCE = 0
    POWER = 1


def balance_heuristic(p1, p2, x, index, start, end):
    if index == 1:
        return p1(x, start, end) / (p1(x, start, end) + p2(x, start, end))
    else:
        return p2(x, start, end) / (p1(x, start, end) + p2(x, start, end))


def power_heuristic(p1, p2, x, index, start, end):
    if index == 1:
        return p1(x, start, end) ** 2 / (p1(x, start, end) ** 2 + p2(x, start, end) ** 2)
    else:
        return p2(x, start, end) ** 2 / (p1(x, start, end) ** 2 + p2(x, start, end) ** 2)
