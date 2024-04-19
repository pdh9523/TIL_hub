# from collections import deque

# DP = deque([0,1])

# N = int(input())

# if N == 0 or N == 1 :
#     print(1 if N == 1 else 0)
#     exit(print(DP[N]))

# elif N < 0 :    # 음수 
#     for _ in range(abs(N)):
#         DP.appendleft((DP[1]-DP[0])%10**9)
#     print(-1 if DP[0] < 0 else 1)
#     print(abs(DP[0]))
# else :          # 양수
#     for _ in range(N):
#         DP.append((DP[-1]+DP[-2])%10**9)
#     print(1)
#     print(DP[-1])

# ### 메모리 초과
    
c,a,b = 1,0,1

N = int(input())


if N == 0 :
    print(0)
    print(0)
    exit()

ans = 1

if N < 0 :
    N = -N
    ans = 1 if N % 2 else -1

for _ in range(N-1):
    c = (a+b) % 10**9
    a,b = b,c

print(ans)
print(c)