N, M = list(input()), list(input())
lenn,lenm = len(N), len(M)

DP = [0] * lenm         # DP의 각 인덱스를 M의 원소라 치고

for i in range(lenn):
    cnt = 0 
    for j in range(lenm):
        if cnt < DP[j]: cnt = DP[j]
        elif N[i] == M[j]: DP[j] = cnt+1
print(max(DP))