# https://open.kattis.com/problems/dasort
# p = number of datasets
# k = data set number
# n = length of array
# positive integers only
# 10 values per line, except for last line which may have less than 10 values

import math

p = int(input())

for _ in range(p):
    k, n = [int(x) for x in input().split(' ')]
    
    j = math.ceil(n / 10)
    l = []

    for _ in range(j):
        l += [int(x) for x in input().split(' ')]
    
    s = sorted(l)

    si = 0

    for item in l:
        if item == s[si]:
            si += 1
    print(f'{k} {len(l) - si}')