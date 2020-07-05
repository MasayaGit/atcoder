import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    S = []

    for _ in range(N):
        S.append(input())
    print("AC"+" x "+ str(S.count('AC\n')))
    print("WA"+" x "+ str(S.count('WA\n')))
    print("TLE"+" x "+ str(S.count('TLE\n')))
    print("RE"+" x "+ str(S.count('RE\n')))


    return


if __name__ == '__main__':
    main()
