# https://open.kattis.com/problems/different

from sys import stdin

for line in stdin:
    line = line.strip().split(" ")
    print(abs(int(line[0]) - int(line[1])))