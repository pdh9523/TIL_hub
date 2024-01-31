rem = [1,0,1,0,1,0,1,0]
chesspan = [] 
for i in range(8) :
    if i % 2 == 0 :
        chesspan.append(rem)
    else : 
        chesspan.append(rem[::-1])

test_case = [list(input()) for _ in range(8)]
count = 0
for x in range(8) :
    for y in range(8) :
        if chesspan[x][y] == 1 and test_case[x][y] == "F" :
            count += 1
print(count)