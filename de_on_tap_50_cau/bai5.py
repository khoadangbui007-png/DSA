import math

def can_finish(piles, h, speed):
    hours = 0

    for p in piles:
        hours += math.ceil(p / speed)

    return hours <= h


def min_speed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        if can_finish(piles, h, mid):
            right = mid
        else:
            left = mid + 1

    return left


piles = [3, 6, 7, 11]
h = 8

print(min_speed(piles, h))