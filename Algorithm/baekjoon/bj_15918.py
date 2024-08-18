# def backtrack(i=1):
#     global cnt
#     if i == N+1:
#         if all(i for i in arr):
#             cnt += 1
#         return
#
#     if i == t:
#         backtrack(i+1)
#     else:
#         for j in range(N*2):
#             if arr[j]: continue
#             if j+i+1 >= 2*N: continue
#             if arr[j+i+1]: continue
#
#             arr[j] = arr[j+i+1] = i
#             backtrack(i+1)
#             arr[j] = arr[j+i+1] = 0
#
#
# N, X, Y = map(int, input().split())
# arr = [0]*N*2
# t = (Y-X-1)
# arr[X-1] = arr[Y-1] = t
# cnt = 0
# backtrack()
# print(cnt)

def backtrack(idx=1):
    global cnt
    if idx == 2*N+1:
        cnt += 1
        return

    if arr[idx] !=0:
        backtrack(idx+1)
        return

    for i in range(1, N+1):
        if not visit[i] and idx+i < 2*N and not arr[idx+i+1]:
            arr[idx]=arr[idx+i+1]=i
            visit[i]=1
            backtrack(idx+1)
            arr[idx]=arr[idx+i+1]=visit[i]=0

N,X,Y = map(int,input().split())

arr = [0]*(2*N+1)
visit = [0]*(N+1)

t = Y-X-1
arr[X] = arr[Y] = t
visit[t] = 1
cnt = 0
backtrack()
print(cnt)