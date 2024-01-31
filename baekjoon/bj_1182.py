a, summary = map(int,input().split())

test_case = list(map(int,input().split()))

count = 0
subset = [[]]
for x in test_case :
    size = len(subset)
    for y in range(size) :
        subset.append(subset[y] + [x])

for i in subset :
    if sum(i) == summary and len(i) >= 1 :
        count += 1
print(count)