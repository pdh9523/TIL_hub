# 플러드 필
# 비스마스킹
# 해싱
# 우선 순위 큐

# min() -> O(N)
# 해싱을 하면서, 해시 테이블을 세개 만들면 더 좋았나? x
# 공간 복잡도를 따질 필요는 없고,
# min()이 아니라, heappush로 저장하는 방식이 조금 더 좋았을 것 같음.

# 떨어져도 할 말 없다.

from heapq import heappush, heappop

visit = [[0]*1005 for _ in range(1005)]
data = dict()
hash_data = dict()

def hashing(arr):
    num = 25
    bt = 0
    for lst in zip(*arr):
        lst = list(lst)[::-1]
        for i in lst:
            bt += i*2**num
            num -= 1
    if bt in num:
        return len(data[hash_data[bt]])


def grouping(arr):
    for _ in range(4):
        num = 25
        bt = 0
        tmp = []
        for lst in zip(*arr):
            lst = list(lst)[::-1]
            tmp.append(lst)
            for i in lst:
                bt += i*2**num
                num -= 1
        arr = tmp   # 깊은 복사 안했음? 헉

def init(N, arr):
    pass

def getCount(arr):
    return hashing(arr)

def getPosition(i,j):
    # return min(data[visit[i][j]])
    return data[visit[i][j]][0]