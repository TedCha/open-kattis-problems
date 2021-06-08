# https://open.kattis.com/problems/yoda

num1 = input()
num2 = input()

num1_len = len(num1)
num2_len = len(num2)

if num1_len < num2_len:
    length = num2_len
    diff = num2_len - num1_len
    num1 = ("0" * diff) + num1
else:
    length = num1_len
    diff = num1_len - num2_len
    num2 = ("0" * diff) + num2

num1_cp = ""
num2_cp = ""

for i in range(length):
    value1 = int(num1[i])
    value2 = int(num2[i])

    if value1 == value2:
        num1_cp += num1[i]
        num2_cp += num2[i]
    elif value1 > value2:
        num1_cp += num1[i]
    elif value2 > value1:
        num2_cp += num2[i]

if num1_cp == "":
    print("YODA")
else:
    print(int(num1_cp))

if num2_cp == "":
    print("YODA")
else:
    print(int(num2_cp))