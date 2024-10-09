import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def add(*num):
    k,v = num
    data[k] = data.get(k,0)+1
    heappush(min_hq, (v,k, data[k]))
    heappush(max_hq, (-v,-k, data[k]))

def recommend(num):
    if num == -1:
        while min_hq[0][1] not in data or (min_hq[0][1] in data and data[min_hq[0][1]] != min_hq[0][2]):
            heappop(min_hq)
        print(min_hq[0][1])
    else:
        while -max_hq[0][1] not in data or (-max_hq[0][1] in data and data[-max_hq[0][1]] != max_hq[0][2]):
            heappop(max_hq)
        print(-max_hq[0][1])


def solved(num):
    data[num] = -1

cmd = {
    "add": add,
    "recommend": recommend,
    "solved": solved
}

max_hq = []
min_hq = []
data = dict()
for _ in range(int(input())):
    k,v = map(int,input().split())
    data[k] = data.get(k,0)+1


    heappush(min_hq, (v,k,data[k]))
    heappush(max_hq, (-v,-k,data[k]))


for _ in range(int(input())):
    c, *d = input().split()
    d = map(int,d)
    cmd[c](*d)