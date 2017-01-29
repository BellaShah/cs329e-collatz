#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cycle_cache = {}
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
    current_cycle = n
    while n > 1 :
        if (n % 2) == 0 :
            n = (n >> 1)
            c += 1
        else :
            n += (n >> 1) + 1
            c += 2
        if n < 1000000 and cache[n] != 0 :
            c+= cache[n]
            break
    n = current_cycle
    cache[n] = c 
    
    assert c > 0
    return c

# ------------
# collatz_eval
# ------------

cache = [0]*1000000
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

    if j < i :
        i, j = j, i
    assert i <= j

    if i < j>>1:
        i = j>>1
    
    for num in range(i, j+1):
        current_cycle = 0
        if cache[num] != 0:
            current_cycle = cache[num]   
        else:
            current_cycle = cycle_length(num)
            if (current_cycle > max_cycle):
                max_cycle = current_cycle
    
    assert max_cycle > 0
    return max_cycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
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
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
