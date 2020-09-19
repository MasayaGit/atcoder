import sys

input = sys.stdin.readline

S = input()
S = S.replace('\n','')
s_list = list(S)

if s_list[-1] == "s":
    new_S = S + "es"
else:
    new_S = S + "s"
    
print(new_S)