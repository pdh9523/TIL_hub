S = list(input())
cnt_0 = S.count('0')//2
cnt_1 = S.count('1')//2

i = 0
while cnt_1 :
    if S[i] == '1' :
        S[i] = ""
        cnt_1 -= 1
    i += 1

i = -1
while cnt_0 :
    if S[i] == '0' :
        S[i] = ""
        cnt_0 -= 1
    i -= 1

print("".join(S).replace(" ", ""))