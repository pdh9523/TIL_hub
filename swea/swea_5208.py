#전기버스

def backtrack(now=0,cnt=-1) :
    global ans
    if cnt >= ans:      # 종료 조건1) cnt가 이미 최소값 이상인 경우
        return          # 가지치기
    
    if now >= end:      # 종료 조건2) 종점에 도착한 경우
        ans = cnt       # ans 를 cnt로 (조건1에 의해 최소값만 전달)
        return
    
    # 백트래킹
    for next in range(1, bus[now]+1):       
        # 현재 버스 배터리로 갈 수 있는 모든 공간에 대한 탐색
        backtrack(now+next,cnt+1)               


for tc in range(int(input())):
    # bus : 정류장 리스트
    end, *bus = list(map(int,input().split()))

    end -= 1            # end : 종점 (인덱스 보정)

    ans = 100           # ans : 최소값을 담을 변수 (최대값 : 리스트의 길이는 최대 100이다.)


    backtrack()
    print(f"#{tc+1} {ans}")