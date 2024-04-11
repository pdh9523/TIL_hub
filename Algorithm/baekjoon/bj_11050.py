a,b = map(int,input().split())
output = 1
for i in range(b) :
    output *= a-i
    output /= i+1
print(int(output))