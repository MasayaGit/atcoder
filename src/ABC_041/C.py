import sys


input = sys.stdin.readline

n = int(input())
a_list = map(int, input().split())
A = []
for i,a in enumerate(a_list):
    index_a = [i+1,a]
    A.append(index_a)

A.sort(key=lambda x: x[1])

for index_a in reversed(A):
    print(str(index_a[0]))