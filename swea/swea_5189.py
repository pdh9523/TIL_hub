# import sys
# sys.stdin = open("5189.txt")
def backtrack(start=0, result = []) :
    global ans
    
    if sum(visit)==size :
        result.append(golf[start][0])
        print(result)
        
        ans.append(sum(result))

    for idx in range(size):
        if idx!=start and visit[idx] == 0 :
            visit[start] =1
            visit[idx]=1
            backtrack(idx, result + [golf[start][idx]])
            visit[idx]=0



for t in range(int(input())):
    size = int(input())
    golf = [list(map(int,input().split())) for _ in range(size)]

    visit = [0] * (size)
    ans = []
    backtrack()
    print(f"#{t+1} {min(ans)}")