N = int(input())
chu = [*map(int,input().split())]

M = int(input())
target = [*map(int,input().split())]

size = max(sum(chu), max(target))+1

DP = {0}
for weight in chu:
    tmp = []
    for i in DP:
        tmp.append(i+weight)
        tmp.append(abs(i-weight))
    DP.update(tmp)
    
for t in target:
    if t in DP: print("Y")
    else : print("N")