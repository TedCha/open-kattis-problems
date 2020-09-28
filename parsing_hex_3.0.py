from sys import stdin
import re

for line in stdin:
    matches = [m.span() for m in re.finditer(r"0[xX][a-fA-F0-9]{1,8}", line)]

    if len(matches) != 0:
        for i in range(len(matches)):
            value = line[matches[i][0]:matches[i][1]]
            print(f"{value} {int(value, 16)}")