a = int(input())

x_value = []
y_value = []
for i in range(a) :
    x,y = map(int,input().split())
    x_value.append(x)
    y_value.append(y)

rkfh = max(x_value) - min(x_value)
tpfh = max(y_value) - min(y_value)

print(rkfh*tpfh)