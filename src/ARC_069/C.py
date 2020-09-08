import sys
import heapq
from decimal import Decimal

input = sys.stdin.readline

n, m = map(int, input().split())

if int(m/2) - n > 0:
    print(n + int((m - 2*n)/4))
else:
    print(int(m/2))