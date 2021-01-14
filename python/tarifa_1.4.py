# https://open.kattis.com/problems/tarifa

x = int(input())
n = int(input())

j = x
for i in range(n):
    j = j - int(input()) + x

print(j)