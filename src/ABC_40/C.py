n = int(input())
n_list = list(map(int, input().split()))
dp = [-1]*n
dp[0] = 0
dp[1] = abs(n_list[1]-n_list[0])

for i in range(2,n):
    #1の時と2の時のどちらがより小さいか
    dp[i] = min(abs(n_list[i]-n_list[i-1])+dp[i-1], abs(n_list[i]-n_list[i-2])+dp[i-2])
print(dp[-1])
