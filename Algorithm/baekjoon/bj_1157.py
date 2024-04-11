a = input().upper()
dic = {}

for i in a :
    if i not in dic :
        dic[i] = 1
    else : 
        dic[i] +=1
count = 0
result = ""
for j in dic : 
    if dic[j] > count :
        count = dic[j]
        result = j
    elif dic[j] == count :
        result = "?"
print(result)