# https://open.kattis.com/problems/metaprogramming

import operator
from sys import stdin

ops = {">": operator.gt, "<": operator.lt, "=": operator.eq}

j = {}

for line in stdin:
    x = line.split()

    if x[0] == 'define':
        j[x[2]] = int(x[1])

    else:
        op_func = ops[x[2]]
        try:
            if op_func(j[x[1]], j[x[3]]):
                print("true")
            elif not op_func(j[x[1]], j[x[3]]):
                print("false")
        except:
            print("undefined")

