import sys

N,M = map(int,input().split())

test_list = [(list(map(int,sys.stdin.readline().strip("\n").split()))) for _ in range(N)]

# 복잡도 최대 1024*1024*100000
## 전처리를 해야한다.
### 0,0 부터 해당 좌표까지의 합을 구한 후 거기서 계산하는 방식으로 전환



for _ in range(M) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip("\n").split())
    output = 0 
    for i in range(y1-1,y2) :
        for j in range(x1-1, x2) :
            output += test_list[i][j]
    print(output)