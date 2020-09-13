import sys

input = sys.stdin.readline

mod = 10**9 + 7
s = int(input())
dp = [0 for i in range(s+1)]
dp[0] = 1

for i in range(1,s+1):
    for j in range(0,(i-3)+1):
        dp[i] += dp[j]
        dp[i] %= mod

print(dp[s])