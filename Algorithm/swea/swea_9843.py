def make(N):
    while arr[-1] < N:
        arr.append((arr[-1]+len(arr)))

arr = [0]

for tc in range(int(input())):
    N = int(input())
    if arr[-1] < N:
        make(N)
    
    print(f"#{tc+1} {len(arr)-1 if arr[-1]==N else -1}")