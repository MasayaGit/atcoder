# -*- coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    h, w, k = map(int, input().split())
    C = []
    for _ in range(h):
        C.append(input())
    ans = 0

    for hbit in range(1<<h): # red row bit h = 2なら 00 ~ 11 100(=2^2)　左ビットシフト 1 -> 100
        for wbit in range(1<<w): # red col bit
            c = 0
            for i in range(h):
                for j in range(w):
                    #9 = 0b1001　を 右ビットシフト　9 >> 1 にすると 100
                    #i, jだけそれぞれ右ビットシフトした時に1になっていたらフラグが立っている.
                    #この実装だと 1だと上書きしないパターン
                    if hbit>>i & 1 and wbit>>j & 1:
                        if C[i][j] =='#': c += 1
            if c == k: ans += 1
    print(ans)

    return


if __name__ == '__main__':
    main()


