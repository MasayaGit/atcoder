import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    if N % 1000 == 0:
        print(0)
    else:
        print(1000 - N % 1000)

    return


if __name__ == '__main__':
    main()
