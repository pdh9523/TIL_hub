import sys
import heapq

def heapverse(lst) :
    minus_lst = list(map(lambda x : -1 * x, lst))
    heapq.heapify(minus_lst)
    return minus_lst


t = int(input())


for _ in range(t):
    i = int(input())
    q = list()

    for _ in range(i):
        order, num = sys.stdin.readline().strip().split()
        num = int(num)
        if order == "I":
            heapq.heappush(q,num)
        if order == "D":
            if len(q) != 0 :
                if num == 1 :
                    q = heapverse(q)
                    heapq.heappop(q)
                    q = heapverse(q)
                if num == -1 :
                    heapq.heappop(q)
    if not q :
        print("EMPTY")
    else :
        min_value = heapq.heappop(q)
        q = heapverse(q)
        max_value = -heapq.heappop(q)
        print(max_value, min_value)