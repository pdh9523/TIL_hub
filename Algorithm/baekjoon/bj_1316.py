a = int(input())
output = 0
for i in range(a) :
    sen = list(input())
    rem = ""
    while sen :
        if len(sen) == 1 :
            rem+= sen[-1]
            break
        elif sen[-1] == sen[-2] :
            sen.pop(-1)
        else : 
            rem += sen[-1]
            sen.pop(-1)
    if len(set(rem)) == len(rem) :
        output+=1
print(output)