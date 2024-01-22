a = 1
for i in range(3) :
    a *= int(input())
result = {}
for j in range(10) :
    result[str(j)] = 0

for k in str(a) :
    result[k] += 1
print(*result.values(), sep="\n")