'''
오일러 회로 조건 :

시작점과 도착점이 같아야 하고, 차수가 홀수인 정점이 없어야 한다. 

문제의 추가 조건 :
두 정점 사이의 간선이 여러개 있을 수 있어, 두 점 사이에 최대 10개의 간선이 있을 수 있다. 

'''

# import sys
# input = sys.stdin.readline

# N = int(input())


# graph = [ [] for _ in range(N+1) ]
# degree = [0] * (N+1)

# for i in range(N) :
#     tmp = [*map(int,input().split())]
#     for j in range(N) :
#         if tmp[j] :
#             graph[i+1].append(j+1)
#             degree[i+1] += 1


# # 차수 홀수 검증
# for i in range(1,N+1):
#     if degree[i] % 2 :
#         print(-1)
#         exit()

# ans = [1]
# stack = [1]
# visit = [ [0]*(N+1) for _ in range(N+1) ]
# check = [0] * (N+1)
# check[0] = 1

# while stack :
#     now = stack.pop()
#     check[now] = 1
#     for next in graph[now] :
#         if not check and not visit[now][next] and degree[next] :
#             visit[now][next] = 1
#             visit[next][now] = 1
#             degree[next] -= 1
#             break
        
#     stack.append(next)
#     ans.append(next)

#     if all(check) :
#         break
# print(*ans)
###처음 생각했던 풀이 (양 점 사이 간선이 하나씩만 존재하는 경우 순회가 가능)

import sys
sys.setrecursionlimit(10**9)

N=int(sys.stdin.readline())

myList=[]

for i in range(N):
    myList.append(list(map(int,sys.stdin.readline().rstrip().split())))

graph={}

for i in range(N):
    graph[i]=[]
    rowSum=0
    for j in range(N):
        for k in range(myList[i][j]):
            rowSum+=1
            graph[i].append(j)
    if rowSum%2==1:
        print(-1)
        sys.exit()

def dfs(nowNode):
    for i in graph[nowNode]:
        if myList[nowNode][i]:
            myList[nowNode][i]-=1
            myList[i][nowNode]-=1
            dfs(i)
    print(nowNode+1,end=" ")

dfs(0)