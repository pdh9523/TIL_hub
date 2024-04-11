_ = int(input())
N = list(map(int,input().split()))
_ = int(input())
M = list(map(int,input().split()))

dic = {i : 1 for i in N}

for item in M:
    print(dic.get(item,0))