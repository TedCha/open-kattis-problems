# https://open.kattis.com/problems/stararrangements
from math import ceil

s = int(input())

print(f"{s}:")
for i in range(2, ceil((s/2))+1):
    if s % (i + (i-1)) == i or s % (i + (i-1)) == 0:
        print(f"{i},{i-1}")
    if s % i == 0:
        print(f"{i},{i}")