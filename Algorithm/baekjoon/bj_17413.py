S = input()
ans, tmp = "", ""

check = True # 괄호 안이면 False
for i in S : 
    if check and i == " ":
        ans += tmp[::-1] + " "
        tmp = ""
        continue

    if i == "<" :
        if check : 
            ans += tmp[::-1]
        else :
            ans += tmp
        tmp = ""
        check = False
    tmp += i
    if i == ">" :
        ans += tmp
        tmp = ""
        check = True
if tmp : 
    if check : 
        ans += tmp[::-1]
    else :
        ans += tmp


print(ans)