s = input() #문자열(baekjoon)
list_s = []
rank = -1
for i in range(26):
    list_s.append(-1)
for j in s : #ord(a) = 97
    rank+=1
    if list_s[ord(j)-97] == -1 :
        list_s[ord(j)-97] = rank
    else : 
        continue
for k in list_s :
    print(k, end=" ")