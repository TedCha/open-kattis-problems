# https://open.kattis.com/problems/tetration
# https://en.wikipedia.org/wiki/Tetration#Infinite_heights
y = float(input())
print(f"{y**(1/y):.6f}")