# https://open.kattis.com/problems/spavanac

h, m = [int(x) for x in input().split()]

m -= 45

if m < 0:
    m += 60
    h -= 1
    if h < 0:
        h += 24

print(f"{h} {m}")