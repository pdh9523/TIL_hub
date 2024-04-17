from heapq import heapify

N = int(input())
arr = list(zip((map(int,input().split())), range(1,N+1)))


# arr[n][0] : 값
# arr[n][1] : 인덱스

heapify(arr)
print(arr)