# https://open.kattis.com/problems/somesum
# 1 : Either
# 2 : Odd
# 3 : Either
# 4 : Even
# 5 : Either
# 6 : Odd
# 7 : Either
# 8 : Even
# 9 : Either
# 10: Odd

n = int(input())

if (n % 2) == 1:
    print("Either")
elif (n % 4) == 0:
    print("Even")
else:
    print("Odd")
