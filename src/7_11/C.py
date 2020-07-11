# -*- coding: utf-8 -*-

import sys
import math

def main():
    input = sys.stdin.readline
    N = int(input())

    result = 0
    ans_list = [0]*(N+1)
    root_n =int(math.sqrt(N))+1

    for i in range(1,root_n):
        for j in range(1,root_n):
            for k in range(1,root_n):
                f = i**2+j**2+k**2+i*j+i*k+j*k
                if f <= N:
                    ans_list[f] += 1 
    
    for i in range(1,N+1):
        print(ans_list[i])
        
                        

    return


if __name__ == '__main__':
    main()