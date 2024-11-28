def merge():
    s = input()
    for i in range(N*K):
        if s[i] != "?":
            merged[i//K] = s[i]

N,M,K = map(int,input().split())

merged = ["?"]*N
for _ in range(M):
    merge()
print("".join(merged))
