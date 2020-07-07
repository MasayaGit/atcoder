# -*- coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    n,m,x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        c.append(row[0])
        a.append(row[1:])
    min_price = -1
    for nbit in range(1<<n): # red row bit h = 2なら 00 ~ 11 100(=2^2)　左ビットシフト 1 -> 100
        sum_price = 0
        sum_a = [0]*m
        for i in range(n):
            if nbit>>i & 1:
                for j in range(m):
                    sum_a[j] += a[i][j]
                sum_price += c[i]
        if sum_price == 0:
            continue
        elif all(value >= x for value in sum_a):
            if min_price == -1:
                min_price = sum_price
            elif sum_price < min_price:
                min_price = sum_price
    
    print(min_price)
    return


if __name__ == '__main__':
    main()

