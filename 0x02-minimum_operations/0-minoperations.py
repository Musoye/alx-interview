#!/usr/bin/python3
'''Minimun  number of Operations
'''


def check(op: int, n: int, val: str) -> int:
    '''serve as helper function'''
    if (op > n):
        return (1)
    elif (len(val) >= n):
        return (2)
    return (0)


def minOperations(n: int) -> int:
    '''Calculate the minimum number of operations'''
    op = 0
    holder = 'H'
    copier = ''
    val = 0
    if (n <= 1):
        return (0)
    for _ in range(2, n + 2):
        if op < 3:
            if op == 0:
                copier = holder
                op += 1
            else:
                holder += copier
                op += 1
        else:
            if n == 4:
                holder += copier
                op += 1
                val += 1
            else:
                if val % 2 == 0:
                    copier = holder
                    op += 1
                    val += 1
                else:
                    holder += copier
                    op += 1
                    val += 1
        if (check(op, n, holder) == 0):
            continue
        elif (check(op, n, holder) > 1):
            return (op)
        elif (check(op, n, holder) == 1):
            return (0)
    return (0)
