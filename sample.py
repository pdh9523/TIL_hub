def consulting(day, can, money):   # 오늘, 마지막 상담일, 현재까지의 수익
    global max_money

    if day > last_day:          # 날짜가 마지막 가능한 상담 날짜를 넘어섰다면
        if max_money < money:   # 최대 수익을 업데이트하고 함수를 종료한다.
            max_money = money
        return

    if day > can:                   # 마지막 상담이 끝났다면,
        print(day, can, money)
        if possible[day][1] == 1:   # 오늘 시작할 수 있는 상담이 당일에 끝나는 상담이라면 무조건 진행한다.
            consulting(day + 1, can + 1, money + possible[day][2])
        else:                       # 오늘 시작할 수 있는 상담이 이틀 이상 걸리는 상담이라면
            consulting(day + 1, can, money)                                         # 1. 상담을 하지 않는다.
            consulting(day + 1, can + possible[day][1], money + possible[day][2])   # 2. 상담을 한다.
    else:                           # 마지막 상담이 끝나지 않았다면, 다음날로 넘어간다.
        consulting(day + 1, can, money)




import sys
input = sys.stdin.readline

N = int(input())
data = [[i] + list(map(int, input().split())) for i in range(N)]   # 날짜, T, P
possible = []

for i in range(N):            # 퇴사전에 끝낼 수 없는 상담 정보 걸러내기
    if i + data[i][1] <= N:
        possible.append(data[i])

print(possible)

max_money, last_day = 0, possible[-1][0]
consulting(0, -1, 0)
print(max_money)