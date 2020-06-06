# https://open.kattis.com/problems/climbingworm

a, b, h = [int(x) for x in input().split()]

x = 0
i = 0

while True:
    x += a
    i += 1
    if x == h:
        break
    elif x >= h:
        break
    else:
        x -= b

print(i)