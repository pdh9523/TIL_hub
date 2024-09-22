N,K = map(int,input().split())
arr = [*map(int,input().split())]
cnt = 0
now = arr[0]
for i in range(N):
    if now + K < arr[i]:
        now = arr[i]
        cnt +=1

print(cnt+1)