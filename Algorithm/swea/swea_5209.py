# 최소생산비용 

def backtrack(idx=0, visit=[], tmp=0):
    global ans

    if tmp >= ans :         # 종료조건1) 가지치기
        return              # 계산 중 나온 최소값보다 높은 값을 계산하고 있을 이유는 없다
    if idx == size :        # 종료조건2) 순회를 마친 경우
        ans = tmp           # 가지치기 조건에 따라 tmp가 최소값인 경우에만 도달 가능
        return

    # 백트래킹
    for i in range(size):
        if i not in visit :                                     # 방문여부 확인
            backtrack(idx+1, visit+[i], tmp+factory[i][idx])    # tmp에 계산된 값을 담고 백트래킹


for tc in range(int(input())):
    # 입력
    size = int(input())
    factory = [list(map(int,input().split())) for _ in range(size)]

    # (최대값 설정) 15개 줄에 걸쳐 최대 99의 생산비용이 든다.
    ans = 1500              

    # 함수 실행 및 출력
    backtrack()
    print(f"#{tc+1} {ans}")