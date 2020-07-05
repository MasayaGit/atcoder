import sys
import math

def main():
    input = sys.stdin.readline
    #1行に複数の入力の時は.split()使う
    AB = input().split()
    A, B = int(AB[0]),int(AB[1].replace(".",""))
    print(A*B // 100)
    return


if __name__ == '__main__':
    main()
