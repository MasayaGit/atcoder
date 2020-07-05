import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int , input().split()))
    max_number = 10 ** 18
    result = 1
    if 0 in A:
        print(0)
        return
    for a in A:
        result = result * a
        if result > max_number:
            print(-1)
            return
    print(result)
    return


if __name__ == '__main__':
    main()
