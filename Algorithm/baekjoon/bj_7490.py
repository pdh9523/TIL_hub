def backtrack(idx=0, sick='1'):
    if idx == N-1 : 
        if eval(sick.replace(' ', '')) == 0 :
            print(sick)
        return
    for i in [' ','+','-']:
        backtrack(idx+1, sick+i+str(idx+2))

for _ in range(int(input())):

    N = int(input())
    backtrack()
    print()