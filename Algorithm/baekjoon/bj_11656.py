S = input()
arr = []
for i in range(len(S)):
    arr.append(S[i:])
print(*sorted(arr), sep= "\n")