# https://open.kattis.com/problems/server

n, t = [int(x) for x in input().split()]

tasks = [int(x) for x in input().split()]

# Local Variable in List Comprehension (https://stackoverflow.com/questions/26672532/how-to-set-local-variable-in-list-comprehension)
# If only kattis used python 3.8! (:=)
print([j for j in (sum(tasks[:(l+1)]) for l, m in enumerate(tasks)) if j <= t])
