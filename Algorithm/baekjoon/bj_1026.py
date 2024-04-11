a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
b.sort()
c.sort(reverse=True)
output = 0
for i in range(a) :
    output += b[i]*c[i]

print(output)