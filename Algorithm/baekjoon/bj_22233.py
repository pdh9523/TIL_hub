# import sys
# input = sys.stdin.readline

# N,M = map(int,input().split())
# data = { input().strip() : True for _ in range(N)}

# for _ in range(M):
#     arr = input().strip().split(",")
#     for char in arr:
#         if data.get(char):
#             data[char] = False
#             N -= 1
#     print(N)


import sys
input = sys.stdin.readline
 
N,M = map(int,input().split())
data = set(input().strip() for _ in range(N))
 
for _ in range(M):
    arr = set(input().strip().split(","))
    data-= arr
    print(len(data))