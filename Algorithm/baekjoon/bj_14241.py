# from heapq import heappop, heappush, heapify

# N = int(input())
# hq = [*map(int,input().split())]

# heapify(hq)

# ans = 0
# while len(hq) > 1:
#     a = heappop(hq)
#     b = heappop(hq)
#     ans += a*b
#     heappush(hq, a+b)
# print(ans)

N=input()
l,t=0,0
for i in map(int,input().split()):l += t*i;t += i
print(l)