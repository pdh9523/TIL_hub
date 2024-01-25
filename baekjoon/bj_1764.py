import sys

a,b = map(int,input().split())

a_set = set()
b_set = set()

for i in range (a) :
    c = input()
    a_set.add(c)

for j in range (b) :
    d = input()
    b_set.add(d)

result = list(a_set & b_set)
result.sort()
print(len(result))
for k in result :
    print(k)