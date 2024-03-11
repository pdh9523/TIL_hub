# import sys 
# from collections import deque

# input = sys.stdin.readline

# N, M = int(input()), int(input())

# city = [list(map(int,input().split())) for _ in range(N)]

# schedule = deque(map(lambda x : int(x)-1, input().split()))

# start = schedule.popleft()
# q = deque([start])

# goal = schedule.popleft()
# visit = [[0] * (N+1) for _ in range(N+1)]
# while q :
#     s = q.popleft()
#     city[start][s] = 1
#     city[s][start] = 1

#     if s == goal:
#         q=deque([goal])
#         start = goal
#         visit = [[0] * (N+1) for _ in range(N+1)]
#         if schedule: 
#             goal = schedule.popleft()
#         else :
#             exit(print("YES"))
    
#     for i in range(N):
#         if city[s][i] == 1 :
#             visit[s][i] == 1
#             q.append(i)
# else :
    # print("NO")

### 시간 초과 + 메모리 초과 쌍으로 맞음
    

## 세트로 풀이하기

# N, M = int(input()), int(input())

# city = [list(map(int,input().split())) for _ in range(N)]
# schedule = set(map(lambda x : int(x)-1, input().split()))
# visit = [] 

# for i in range(N-1):
#     for j in range(i,N):
#         if city[i][j] == 1:
#             if visit :
#                 for item in visit :
#                     if item & {i,j} :
#                         item.update({i,j})
#                     else:
#                         visit.append({i,j})
#             else:
#                 visit.append({i,j})
# for i in visit :
#     if schedule.issubset(i) :
#         exit(print("YES"))
# else :
#     print("NO")

### 이것도 메모리 초과 ㅋㅋㅋㅋㅋ