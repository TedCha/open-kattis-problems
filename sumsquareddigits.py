# https://open.kattis.com/problems/sumsquareddigits

for j in range(int(input())):
    k, b, n = [int(x) for x in input().split()]

    ssd = 0
    while n > 0:
        ssd += (n % b) * (n % b)
        n //= b
    
    print(f"{k} {ssd}")

    
