S = input()
N = int(input())
arr = [input() for _ in range(N)]
data = {v: len(v) for v in arr}

length = len(S)
DP = [float("inf")]*(length+1)
DP[0] = 0

for i in range(length+1):
    for char in data:
        if i-data[char]<0:continue
        if sorted(list(char))!=sorted(list(S[i-data[char]:i])) : continue

        tmp = 0
        for a,b in zip(char, S[i-data[char]:i]):
            if a!=b: tmp += 1

        DP[i] = min(DP[i], DP[i-data[char]]+tmp)
print(DP[-1] if DP[-1] != float("inf") else -1)
