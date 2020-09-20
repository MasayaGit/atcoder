import sys

input = sys.stdin.readline

n = int(input())

b_list = list(map(int, input().split()))
result_list = []
while len(b_list) > 0:
    flag = False
    for i,b in enumerate(reversed(b_list)):
        if len(b_list)-i == b:
            result_list.append(b)
            b_list.pop(len(b_list)-i -1)
            flag = True
            break
    if not flag:
        print(-1)
        exit(0)

for b in reversed(result_list):
    print(b)
    
    
