#!/usr/bin/python3
"""making changes Interview Question"""


def makeChange(coins, total):
    """makeChange interview question function"""
    if total <= 0:
        return 0
    hel = 0
    number = 0
    helping = 0
    holder = total
    coins = sorted(coins, reverse=True)
    for m in coins:
        hel = total // m
        helping += hel * m
        number += hel
        total -= (hel * m)
        if (helping == holder):
            return (number)
        elif (total > holder):
            return (-1)
        else:
            continue
    return (-1)
