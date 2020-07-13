# -*- coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    n,m = map(int, input().split())
    #大人でループする
    for i in range(n+1):

        zero_child_i = n - i
        sum_m = i * 2 + zero_child_i * 4
        if sum_m == m:
            print(str(i)+" "+str(0)+" "+str(zero_child_i))
            exit(0)

        one_child_i = n - i - 1
        sum_m = i * 2 + one_child_i * 4 + 3
        if sum_m == m:
            if i == n:
                break
            print(str(i)+" "+str(1)+" "+str(one_child_i))
            exit(0)

    print("-1 -1 -1")
        
    return


if __name__ == '__main__':
    main()