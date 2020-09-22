import sys

input = sys.stdin.readline

n, k= map(int, input().split())

sum_a_list = [0 for i in range(n)]
a_list = list(map(int, input().split()))
sum_a_list[0] = a_list[0]

for i in range(1,n):
    sum_a_list[i] += sum_a_list[i-1] + a_list[i]

result = 0
for i in range(0,n-k+1):
    if i == 0:
        result += sum_a_list[k-1]
    else:
        result += sum_a_list[k+i-1] - sum_a_list[i-1]

print(result)
