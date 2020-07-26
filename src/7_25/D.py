n = int(input())

a_list = list(map(int, input().split()))
dp_list = [0]*n
dp_list[0] = 1000
for i in range(1,n):
    dp_list[i] = dp_list[i-1]
    for j in range(i):
        v = int(dp_list[j]/a_list[j])
        w = dp_list[j] + (a_list[i] - a_list[j]) * v
        dp_list[i] = max(dp_list[i],w)

print(dp_list[n-1])

