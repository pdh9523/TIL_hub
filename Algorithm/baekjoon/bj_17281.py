import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

line = [list(map(int,input().split())) for _ in range(N)]

ans = 0

for order in permutations(list(range(1,9)),8) :
    order = list(order)
    order.insert(3,0)
    score = 0
    idx = 0 
    for inning in range(N):
        out = 0
        base1=0
        base2=0
        base3=0

        while out < 3 :
            # 타자
            hitter = line[inning][order[idx]]
            # 아웃
            if hitter == 0 :
                out += 1
            # 1루타
            elif hitter == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            # 2루타
            elif hitter == 2 :
                score += base3+base2
                base3 = base1
                base2 = 1
                base1 = 0
            # 3루타
            elif hitter == 3 :
                score += base3+base2+base1
                base3 = 1
                base2 = 0
                base1 = 0
            # 홈런
            elif hitter == 4 :
                score += base3+base2+base1+1
                base3=0
                base2=0
                base1=0
            # 인덱스는 교체하지않고 9로 나누면서 계속 진행
            idx = (idx+1)%9

    ans = max(ans,score)
print(ans)