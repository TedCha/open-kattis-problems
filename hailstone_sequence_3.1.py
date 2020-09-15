# https://open.kattis.com/problems/hailstone
x = int(input())

y = []

def hailstone_seq(n):
    y.append(n)
    if n == 1:
        return 1
    # Even
    elif n % 2 == 0:
        return hailstone_seq(n//2)
    # Odd
    else:
        return hailstone_seq((3*n)+1)

hailstone_seq(x)
print(sum(y))