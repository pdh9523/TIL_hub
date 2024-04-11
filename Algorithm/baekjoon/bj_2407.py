import math

n,m = map(int,input().split())
if m > n/2 :
    m = n-m
output = 1
for i in range(m) :
    output *= n-i

for j in range(1,m+1) :
    output /= j

print(round(output))