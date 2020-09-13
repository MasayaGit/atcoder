import sys

input = sys.stdin.readline

n = int(input())

x, y= map(int, input().split())

a_list = list(map(int, input().split()))

h_list = []
for _ in range(n):
    h_list.append(int(input()))

for _ in range(M):
    a, b = map(int, input().split())


S = input()
S = S.replace('\n','')
s_list = list(S)
