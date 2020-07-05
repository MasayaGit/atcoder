#N
#A1 B1
#A2 B2
#.  .
#AN BN

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        print("#####")
        print(a)

    A.sort()
    B.sort()

    if N & 1:
        j = (N - 1) // 2
        ans = B[j] - A[j] + 1
        print(ans)
        return

    j = N // 2 - 1
    k = N // 2
    ans = (B[j] + B[k]) - (A[j] + A[k]) + 1
    print(ans)
    return


if __name__ == '__main__':
    main()
