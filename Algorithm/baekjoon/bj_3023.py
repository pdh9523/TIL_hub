N,M = map(int,input().split())
arr = []

for _ in range(N):
    S = input()
    S = S+S[::-1]
    arr.append(S)

for i in arr[::-1]:
    arr.append(i)

N,M = map(lambda x: int(x)-1,input().split())

tmp = list(arr[N])
tmp[M] = "#" if arr[N][M] == "." else "."
tmp = "".join(tmp)
arr[N] = tmp

print(*arr, sep="\n")