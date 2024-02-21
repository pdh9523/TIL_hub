import heapq

t = int(input())
for idx in range(t):
    N = int(input())
    numbers = list(map(int, input().split()))

    heap = []
    parent_sum = 0
    
    for num in numbers:
        heapq.heappush(heap, num)
    
    heap.insert(0,0)

    while N != 0 :
        parent_sum += heap[(N//2)]
        N //=2
    print(f"#{idx+1} {parent_sum}")