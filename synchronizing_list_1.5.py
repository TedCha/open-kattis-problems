# https://open.kattis.com/problems/synchronizinglists
while True:
    n = int(input())
    n2 = 2 * n

    if n == 0:
        break
    
    list1 = []
    list2 = []

    for i in range(1, n2 + 1):
        x = int(input())
        if i <= n:
            list1.append(x)
        if i > n:
            list2.append(x)

    sortedList1 = sorted(list1)
    list2.sort()

    syncMap = {sortedList1[i]: list2[i] for i in range(n)}
    
    for value in list1:
        print(syncMap[value])
    print("")
    