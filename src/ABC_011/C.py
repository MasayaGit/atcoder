import sys

input = sys.stdin.readline

n = int(input())

ng_list = []
for _ in range(3):
    ng_list.append(int(input()))

dp = [10**5 for _ in range(n+1)]
dp[n] = 0

for i in reversed(range(n+1)):
    if i in ng_list:
        continue
    for number in range(1,4):
        if i - number >= 0:
            dp[i-number] = min(dp[i]+1,dp[i-number])

if dp[0] <= 100:
    print("YES")
else:
    print("NO")