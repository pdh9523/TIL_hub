N = int(input())
K = int(input())
arr = sorted([*map(int,input().split())])
if N > K:
    distance = sorted([arr[i]-arr[i-1] for i in range(1,N)])
    print(sum(distance[:N-K+1]))
else: print(0)