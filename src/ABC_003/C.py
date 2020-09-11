import sys
input = sys.stdin.readline

n,k = map(int, input().split())
r_list = map(int, input().split())
sort_r_list = sorted(r_list, reverse=True)
limit_sort_r_list = sort_r_list[:k]

result = 0
for r in reversed(limit_sort_r_list):
    result += r
    result = result / 2
print(result)