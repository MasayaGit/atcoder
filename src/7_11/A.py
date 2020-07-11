# -*- coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    l,r,d = map(int, input().split())
    l_count = l // d
    r_count = r // d
    result = 0
    if l % d == 0:
        print(r_count - l_count + 1)
    else:
        print(r_count - l_count)

    return


if __name__ == '__main__':
    main()