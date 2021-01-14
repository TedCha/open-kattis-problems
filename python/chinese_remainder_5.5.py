# https://open.kattis.com/problems/chineseremainder

# Extended Eluclid's Algorithm - https://www.kkhaydarov.com/greatest-common-divisor-python/
# returns Bézout coefficients
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

t = int(input())

for i in range(t):
    a, n, b, m = [int(x) for x in input().split()]
    k = n*m

    d, u, v = egcd(n, m)

    # CRT Wikipedia - https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    # Under 'Existence (constructive proof)'
    x = (b*u*n + a*v*m) % k

    print(f'{x} {k}')