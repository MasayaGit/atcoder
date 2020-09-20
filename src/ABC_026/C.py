import sys

input = sys.stdin.readline

n = int(input())


b_buka_dict = {}
b_money_dict = {}
for i in range(1,n+1):
    b_buka_dict[i] = []
    b_money_dict[i] = 1

for i in range(1,n):
    zyousi = int(input())
    b_buka_dict[zyousi].append(i+1)


for i in reversed(range(1,n+1)):
    if len(b_buka_dict[i]) == 0:
        continue
    else:
        buka_list = b_buka_dict[i]
        min_money = 10**6
        max_money = 0
        for buka_id in buka_list:
            buka_money = b_money_dict[buka_id]
            min_money = min(min_money,buka_money)
            max_money = max(max_money,buka_money)
        b_money_dict[i]= min_money+max_money+1

print(b_money_dict[1])

