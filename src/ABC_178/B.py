import sys

input = sys.stdin.readline

a, b, c, d= map(int, input().split())
ac = a*c
ad = a*d
bc = b*c
bd = b*d
max_1 = max(ac,ad)
max_2 = max(bc,bd)
ans = max(max_1,max_2)
print(ans)
