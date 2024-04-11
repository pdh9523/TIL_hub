# t = int(input())


# for _ in range(t):
#     i = int(input())
#     q = list()
#     minusq = list()

#     length = 0
#     for _ in range(i):
#         order, num = sys.stdin.readline().strip().split()
#         num = int(num)
#         if order == "I":
#             heapq.heappush(q,num)
#             heapq.heappush(minusq,-num)      
#             length +=1
#         if order == "D" and length > 0 :
#             if num == 1 :
#                 heapq.heappop(minusq)
#             else :
#                 heapq.heappop(q)
#             length -=1 

#     if length <= 0  :
#         print("EMPTY")
#     else :
#         min_value = heapq.heappop(q)
#         max_value = -heapq.heappop(minusq)
#         print(max_value, min_value)
import sys
import heapq

t = int(input())

for _ in range(t):
    min_heap = []           # 최소힙과 최대힙을 구분
    max_heap = []
    visit = [0] * 1000001   # 최대가 100만개로, 방문 표시를 해 추가적으로 삭제
    K = int(input())
    for idx in range(K):
        order, num = sys.stdin.readline().strip().split()
        num = int(num)

        if order == "I":
            heapq.heappush(min_heap, [num,idx])
            heapq.heappush(max_heap, [-num,idx])
            visit[idx] = 1      # 푸시한 경우 그 인덱스에 숫자가 있음을 나타내고, 
                                # 삭제 명령에서 visit를 0으로 돌려 그 인덱스가 삭제되었음을 알림
        elif order == "D":
            if num == 1:        # 1 : 최대값 삭제
                while max_heap and visit[max_heap[0][1]]==0:    # 인덱스가 삭제된 경우 계속 삭제
                    heapq.heappop(max_heap)
                if max_heap:                                    # while 반복이 끝난 후 타겟을 다시 삭제 
                    visit[max_heap[0][1]] = 0                   
                    heapq.heappop(max_heap)

            elif num == -1:
                while min_heap and visit[min_heap[0][1]]==0:    # 최소힙 연산도 동일 
                    heapq.heappop(min_heap)
                if min_heap:    
                    visit[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    # 반복이 끝난 후 남아 있는 삭제된 값들 정리
    while max_heap and visit[max_heap[0][1]]==0:
        heapq.heappop(max_heap)
    while min_heap and visit[min_heap[0][1]]==0:
        heapq.heappop(min_heap)
    
    # 출력
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else :
        print("EMPTY")

# 321344kb / 10016ms