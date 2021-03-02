# https://open.kattis.com/problems/fromatob

def transform(a, b):
    if a == b:
        return 0
        
    if b > a:
        return b - a
    
    if (a % 2) == 1:
        return 1 + transform(a + 1, b)
    
    else:
        return 1 + transform(a//2, b)


a, b = [int(x) for x in input().split()]
minOperations = transform(a, b)

print(minOperations)
