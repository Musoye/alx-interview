#!/usr/bin/python3
"""The prime game for winner"""
import math


def is_prime(n):
    """check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    val = math.isqrt(n)
    for d in range(3, val + 1, 2):
        if n % d == 0:
            return False
    return True


def gen_prime(prime_lis):
    """genearet prime from a list"""
    prime = []
    for val in prime_lis:
        if is_prime(val):
            prime.append(val)
    return prime


def gen_factor(p, p_list):
    """generate factor of a prime"""
    new_list = []
    new_list.append(p)
    for val in p_list:
        if val % p:
            new_list.append(val)
    return new_list


def isWinner(x, nums):
    '''The prime game to determine the winner'''
    playe = ['X', 'Y']
    player = {'X': 0,  'Y': 0}
    for i in range(x):
        number = nums[i]
        num_lis = range(1, number)
        prime = gen_prime(num_lis)
        for j, v in enumerate(prime):
            prime_fact = gen_factor(v, num_lis)
            num_lis = [r for r in num_lis if r not in prime_fact]
        number = ((len(prime) + 1) % 2)
        print(f'number : {number}')
        player[playe[number]] += 1
    if player['X'] > player['Y']:
        return "Maria"
    return "Ben"
