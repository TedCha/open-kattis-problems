# https://open.kattis.com/problems/primaryarithmetic

from sys import stdin

for line in stdin:
    a, b = line.split()

    if a == '0' and b == '0':
        break

    a = a.zfill(10)
    b = b.zfill(10)

    a = a[::-1]
    b = b[::-1]

    c = 0
    carry = 0

    for i in range(10):
        if int(a[i]) + int(b[i]) + carry > 9:
            c += 1
            carry = 1
        else:
            carry = 0
    
    if c == 0:
        print("No carry operation.")
    elif c == 1:
        print(f"1 carry operation.")
    elif c > 1:
        print(f"{c} carry operations.")