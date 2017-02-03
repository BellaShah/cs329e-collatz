#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

cache = [0] * 1000001

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

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]

    Used a fixed array to store cycle lengths for each value upon computation
    Sphere accepted
    """
    assert i > 0
    assert j > 0

    max_cycle = 0
    current_cycle = 0
    cache[1] = 1

    if j < i:
        i, j = j, i
    assert i <= j

    if i < j >> 1:
        i = j >> 1

    for num in range(i, j + 1):
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

                if (num <= 1000000 and cache[num] != 0):
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
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
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
