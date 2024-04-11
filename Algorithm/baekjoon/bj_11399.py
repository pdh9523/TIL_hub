import sys

a = int(input())

b = list(map(int,sys.stdin.readline().split()))

b.sort(reverse=True)
output = 0
for i in range(len(b)) :
    output += (i+1)*b[i]

print(output)