N = int(input())

alphabet = [input() for _ in range(N)]

position = [[] for _ in range(8)]
for idx in range(7,-1,-1) :
    for char in alphabet:
        if len(char) > idx :
            position[idx].append(char[-idx-1])

nums = list(range(10))
result = {}

for i in range(7,-1,-1):
    counter = {}

    for alpha in position[i]:
        counter[alpha] = counter.get(alpha,0)+1

    for tmp in sorted(counter.keys(), key= lambda x : -counter[x]):
        if tmp not in result :
            result[tmp] = nums.pop()

for j in range(8):
    position[j] = list(map(lambda x: result[x], position[j]))
position = list(map(sum,position))

ans = 0
for i in range(8) :
    ans += position[i] * 10 ** i
print(ans)
