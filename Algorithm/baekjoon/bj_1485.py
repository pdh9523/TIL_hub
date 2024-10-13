import sys; input = sys.stdin.readline


def cal(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


def is_square(arr):
    data = dict()
    for i in range(3):
        for j in range(i+1,4):
            tmp = cal(arr[i], arr[j])
            data[tmp] = data.get(tmp, 0)+1
    return len(data) == 2 and sorted(data.values()) == [2,4]


for _ in range(int(input())):
    print(int(is_square([[*map(int,input().split())] for _ in range(4)])))