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

#N
#t1 x1 y1t1 x1 y1
#t2 x2 y2t2 x2 y2
#⋮⋮
#tN xN yNtN xN yN
N = int(input())
t = [0 for i in range(N)]
x = [0 for i in range(N)]
y = [0 for i in range(N)]
for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

#L1 R1
#L2 R2
#⋮⋮
#Lk Rk
LR = [list(map(int, input().split())) for i in range(K)]
for l, r in LR:
    print(l,r)