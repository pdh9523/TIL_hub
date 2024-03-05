from collections import deque

N,K = map(int,input().split())

belt = deque(map(int,input().split()))

robot = deque([0]*(2*N))

cnt = 1 # 1단계부터 시작함

## 벨트는 계속 회전하고, 로봇은 1단계 당 한칸씩 움직일 수 있음
while True:
    # 1) 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    # 회전하면서 N에 로봇이 들어가면 내린다
    if robot[N-1] == 1:
        robot[N-1] = 0 
    # 2) 가장 먼저 벨트에 올라간 로봇부터? (뒤에 있는 로봇부터)
    # 벨트가 회전하는 방향으로 이동할 수 있다면 이동한다
    # 이동 코스트 : 앞에 로봇이 없고 가는 칸의 내구도가 1 이상

    for i in range(N,-1,-1):

        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0 :
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    # 회전하면서 N에 로봇이 들어가면 내린다    
    if robot[N-1] == 1:
        robot[N-1] = 0 

    # 3) 올리는 위치에 있는 칸의 내구도가 0이 아니면, 올리는 위치에 로봇을 올린다.
    if belt[0] > 0 :
        robot[0] = 1 # 로봇 올렸습니다
        belt[0] -= 1

    # 4) 내구도 0이 K이상이면 종료
    if belt.count(0) >= K :
        break
    cnt += 1

print(cnt)