from itertools import combinations

def findA(x):
    return 1-(x[0]^x[1])

def cal(x):
    return 1 if sum(x)>len(x)/2 else 0

def ensemble(args):
    return sum(map(findA, zip(ans,list(map(cal,zip(*args))))))

N,M = map(int,input().split())
# 정답
ans = [*map(int,input().split())]
# 학생들의 예측치
stdnts = [[*map(int,input().split())] for _ in range(N)]

# 정확도 
accuracy = 0 
for stdnt in stdnts :
    accuracy = max(accuracy,sum(map(findA , zip(stdnt,ans))))
# 비교 
for i in range(3,N+1,2):
    for comb in combinations(stdnts,i):
        if accuracy < ensemble(comb):
           exit(print(1))
print(0)