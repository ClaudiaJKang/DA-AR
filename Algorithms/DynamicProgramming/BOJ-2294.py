from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
coin = [int(read()) for i in range(n)]

dp = [0] * (k + 1)

for i in range(1, k + 1):
    a = []

    for j in coin:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])

    dp[i] = min(a) + 1 if a else -1

print(dp[k])
