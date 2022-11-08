#!/usr/bin/env python

import sys
import csv
import pandas as pd
import numpy as np
import math

#region Hey

def count(L):
    return len(L)

def mean(L):
    if (len(L) == 0):
        return math.nan
    s = 0
    for x in L:
        s += x
    return s / len(L)

def std(L):
    avg = mean(L)
    if (math.isnan(avg)):
        return math.nan
    var = 0
    for x in L:
        var += (avg - x) ** 2
    var /= len(L) - 1
    return math.sqrt(var)

def ft_min(L):
    m = math.nan
    for u in L:
        if (math.isnan(m) or u < m):
            m = u
    return m

def ft_max(L):
    m = math.nan
    for u in L:
        if (math.isnan(m) or u > m):
            m = u
    return m

def percentile(L, p):
    if (len(L) < 2):
        return math.nan
    L = list(L)
    L.sort()
    rank = p * (len(L) - 1)
    idx = int(rank)
    m = L[idx + 1] - L[idx]
    b = L[idx]
    return m * (rank - idx) + b

#endregion
    
def tritl(s, maxLen):
    if (len(s) <= maxLen):
        return s
    return s[:maxLen - 2] + '..'

summaries = [
    ("Count", count),
    ("Mean", mean),
    ("Std", std),
    ("min", ft_min),
    ("25%", lambda L : percentile(L, 0.25)),
    ("50%", lambda L : percentile(L, 0.50)),
    ("75%", lambda L : percentile(L, 0.75)),
    ("max", ft_max),
]

MAX_COL_LEN = 18
MIN_COL_LEN = 8

def get_key_paddings(df, key):
    pad = min(max(len(key), MIN_COL_LEN), MAX_COL_LEN)
    return pad

def describe(df):
    numeric_keys = [key for key in df.keys() if np.issubdtype(df[key].dtype, np.number)]
    print(f"{'':7.7}", end="")
    paddings = {}
    for key in numeric_keys:
        pad = get_key_paddings(df, key)
        paddings[key] = pad
        
        print(f"{tritl(key, MAX_COL_LEN):>{pad}}  ", end="")
    print("")
    
    for summary_fn in summaries:
        print(f"{summary_fn[0]:7.7}", end="")
        for key in numeric_keys:
            pad = paddings[key]
            print(f"{float(summary_fn[1](df[key].dropna())):>{pad}.3f}  ", end="")
        print("")



if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [filename.csv]")
    exit()


df = pd.read_csv(sys.argv[1])
describe(df)
