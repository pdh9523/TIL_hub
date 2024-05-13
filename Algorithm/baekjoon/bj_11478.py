S = input()
ans = set()
length = len(S)
for i in range(length):
    for j in range(length):
        if i+j > length:
            break
        ans.add(S[i:i+j])
print(len(ans))