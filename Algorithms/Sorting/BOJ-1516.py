from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
building = [[] for i in range(n + 1)]
time = [0] * (n + 1)
con = [0] * (n + 1)

for i in range(1, n + 1):
    l = list(map(int, read().split()))
    time[i] = l[0]

    for j in l[1:]:
        if j == -1: break
        building[j].append(i)
        con[i] += 1

q = deque()
res = [0] * (n + 1)
for i in range(1, n + 1):
    if con[i] == 0:
        res[i] = time[i]
        q.append(i)

for i in range(1, n + 1):
    cur = q.popleft()

    for j in building[cur]:
        con[j] -= 1
        res[j] = max(res[j], res[cur] + time[j])

        if con[j] == 0:
            q.append(j)

print('\n'.join(map(str, res[1:])))