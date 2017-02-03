#!/usr/bin/env python3

# ---------------------------
# projects/collatz/SphereCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# -------
# imports
# -------

import sys

cache = [0]*1000001

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]



def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n >> 2)
            c += 1
        else :
            n += (n >> 1) + 1
            c += 2
    assert c > 0
    return c

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j > 0
    
    max_cycle = 0
    current_cycle = 0
    cache[1] = 1

    if j < i :
        i, j = j, i
    assert i <= j

    if i < j >> 1:
        i = j >> 1

    for num in range(i, j+1):
        current_cycle = 0
        orig_num = num
        if (cache[num] != 0):
            current_cycle = cache[num]   
        else:
            while num > 1:
                if (num % 2 == 0):
                    num >>= 1
                    current_cycle += 1
                else:
                    num += (num >> 1) + 1
                    current_cycle += 2

                if (num <= 1000000 and cache[num]!= 0):
                    current_cycle = current_cycle + cache[num]
                    break
        cache[orig_num] = current_cycle

        if current_cycle > max_cycle:
            max_cycle = current_cycle
    
    assert max_cycle > 0
    return max_cycle




# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if not s.strip():
            continue
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""