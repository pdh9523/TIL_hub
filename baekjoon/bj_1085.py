x,y,w,h = map(int,input().split())

if x < abs(x-w) :
    x_value = x
else :
    x_value = abs(x-w)
if y < abs(y-h) :
    y_value = y
else : 
    y_value = abs(y-h)

print(min(x_value, y_value))