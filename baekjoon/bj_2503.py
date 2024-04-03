
N = int(input())

question = []

for _ in range(N):
    q, strike, ball = input().split()
    q = list(map(int,list(q)))
    strike = int(strike)
    ball = int(ball)
    question.append([q,strike,ball])

cnt = 0                                             # cnt : 정답인 경우 증가시킬 카운트
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if len({a,b,c}) == 3:                   # 조건 : 서로 다른 숫자 3개로 구성된
                num = [a,b,c]                       # 완전 탐색

                for i in range(N):                  # 위에서 저장한 질문들을 순회하면서
                    st = 0                          # 지금 비교 중인 숫자의 strike 개수
                    ba = 0                          # 지금 비교 중인 숫자의 ball 개수
                    q, strike, ball = question[i]
                    for idx in range(3):
                        if num[idx] == q[idx] :     # 값과 위치가 같으면 st += 1
                            st += 1
                        if num[idx] == q[idx-1]:    # 값은 같은데 위치가 다르면 ba += 1 
                            ba += 1
                        if num[idx] == q[idx-2]:
                            ba += 1
                    if st != strike :               # 비교중인 숫자의 스트라이크 개수가 서로 다르면 break
                        break
                    if ba != ball :                 # 비교중인 숫자의 볼 개수가 서로 다르면 break
                        break
                else:                               # 모든 순회가 가능하고, 둘다 다르지 않으면 cnt += 1
                    cnt += 1

print(cnt)
