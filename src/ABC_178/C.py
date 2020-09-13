import sys

#a^n mod p を求める
def power_func(a,n,p):
    bi = str(format(n,"b"))#2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res*res) %p
        if bi[i] == "1":
            res = (res*a) %p
    return res

input = sys.stdin.readline

n = int(input())
p = 1000000007
n_10 = power_func(10,n,p)
n_9 = power_func(9,n,p) * 2 % p

n_8 = power_func(8,n,p)

if n_10 - n_9 + n_8 < 0:
    print(n_10 - n_9 + n_8 + p)
else:
    print(n_10 - n_9 + n_8)





