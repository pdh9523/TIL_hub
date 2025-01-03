from itertools import permutations

def join(t):
    return "".join(t)

data = dict()
data["0"] = [
    [0,0,0,0,0,0],
    [0,0,1,1,0,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,0,0],
    [0,0,0,0,0,0]
]
data["1"] = [
    [0,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,1,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0]
]
data["2"] = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,1,1,1,1,0],
    [0,1,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,0,0,0]
]
data["3"] = [
    [0,0,0,0,0,0],
    [0,1,1,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [0,1,1,1,0,0],
    [0,0,0,0,0,0]
]
data["4"] = [
    [0,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,1,1,0,0],
    [0,1,0,1,0,0],
    [1,1,1,1,1,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0]
]
data["5"] = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,1,0,0,0,0],
    [0,1,1,1,0,0],
    [0,0,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,0,0]
]
data["6"] = [
    [0,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [0,1,1,1,1,0],
    [0,1,0,0,1,0],
    [0,1,1,1,1,0],
    [0,0,0,0,0,0]
]
data["7"] = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0]
]
data["8"] = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,1,0,0,1,0],
    [0,1,1,1,1,0],
    [0,1,0,0,1,0],
    [0,1,1,1,1,0],
    [0,0,0,0,0,0]
]
data["9"] = [
    [0,1,1,1,1,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0]
]

arr = [[*map(int, list(input()))] for _ in range(7)]
cnt = len(arr[0])//6

num = ""
for i in range(cnt):
    tmp = []
    for j in range(7):
        tmp.append(arr[j][i*6:(i+1)*6])
    for i in data:
        if data[i] == tmp:
            num += i
perm = sorted(map(join, permutations(num,len(num))))
idx = perm.index(num)
ans = []

if len(perm) > idx+1:
    for char in perm[idx+1]:
        ans.append(data[char])
    for i in zip(*ans):
        for j in i:
            print(*j, sep="",end="")
        print()
        
else:
    print("The End")