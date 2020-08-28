# https://open.kattis.com/problems/thanos

# p = population
# r = rate of growth (multipler per year)
# f = food production in tons
# All food produced in a year must be consumed that year
# Each individual consumes 1 ton of food a year
# Population is counted as a whole number; rounded down

def sustainability_check(p, r, f, count=0):
    j = int(p) * (int(r)**count)
    if j > int(f):
        return count
    else:
        return sustainability_check(p, r, f, count+1)

n = int(input())

for i in range(n):
    p, r, f = input().split(' ')
    
    print(sustainability_check(p, r, f))