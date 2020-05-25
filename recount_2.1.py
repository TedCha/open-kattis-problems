#https://open.kattis.com/problems/recount

from collections import Counter

v_list = []

while True:
    x = str(input())
    if x != '***':
        v_list.append(x)
    else:
        break

count = Counter(v_list)

max_1 = list(sorted(count.values()))[-1]
max_2 = list(sorted(count.values()))[-2]

if max_1 == max_2:
    print('Runoff!')
else:
    print(max(count, key = count.get))
