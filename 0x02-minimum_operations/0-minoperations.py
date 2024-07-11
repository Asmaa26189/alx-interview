#!/usr/bin/python3
""" minOperations"""


def minOperations(n: int) -> int:
    """ minOperations """
    nxt = 'H'
    bdy = 'H'
    count = 0
    while (len(bdy) < n):
        if n % len(bdy) == 0:
            count += 2
            nxt = bdy
            bdy += bdy
        else:
            count += 1
            bdy += nxt
    if len(bdy) != n:
        return 0
    return count