import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [0]*(N+1)

for _ in range(M):
    a,s,e = map(int,input().split())
    
    if s<arr[a] : 
        print("NO")
    else :
        print("YES")
        arr[a]=e