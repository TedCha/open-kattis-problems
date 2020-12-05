# https://open.kattis.com/problems/simonsays

for i in range(int(input())):
    statement = input()
    prefix = "Simon says "
    if statement.startswith(prefix):
        command = statement[statement.index(prefix) + len(prefix):]
        print(command)