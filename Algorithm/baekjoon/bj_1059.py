L = int(input())
arr = [0]+sorted(map(int,input().split()))
N = int(input())

idx = -1
for i in range(L):
    if arr[i] < N < arr[i+1]:
        idx = i
        break

start = arr[i]
end = arr[i+1]
cnt = 0

for i in range(start+1,end-1):
    for j in range(i+1,end):
        if i<=N<=j:cnt+=1
print(cnt)