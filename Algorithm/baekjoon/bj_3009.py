x_value = {}
y_value = {}

for i in range(3) :
    x,y = map(int, input().split())
    if x not in x_value :
        x_value[x] =1
    else : 
        x_value[x] += 1
    
    if y not in y_value :
        y_value[y] = 1
    else :
        y_value[y] += 1

for key in x_value :
    if x_value[key] == 1:
        print(key, end=" ")
for key in y_value :
    if y_value[key] == 1:
        print(key)