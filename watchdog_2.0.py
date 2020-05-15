#https://open.kattis.com/problems/watchdog

import math
from itertools import product

def max_dist(x1, y1, list):
    distance = 0
    for x2, y2 in list:
        new_distance = (x2-x1)**2 + (y2-y1)**2

        if new_distance > distance:
            distance = new_distance
    return math.sqrt(distance)

test_case = int(input())

for i in range(test_case):
    s,h = map(int, input().split())

    xy_list = []
    for j in range(h):
        xy_list.append(list(map(int, input().split())))
    
    leash_coords = []
    test_list = list(product(range(s), range(s)))
    for x,y in test_list:
        if [x, y] not in xy_list:
            dist = max_dist(x, y, xy_list)
            if x + dist <= s and x - dist >= 0:
                if y + dist <= s and y-dist >= 0:
                    if [x,y] not in xy_list:
                        leash_coords.append((x,y))
                        break

    if len(leash_coords) == 0:
        print('poodle')
    else:
        print(str(leash_coords[0][0]) + ' ' + str(leash_coords[0][1]))