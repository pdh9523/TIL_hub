N = int(input())
arr = [*map(int,input().split())]
# 양 끝 폭죽 더미를 제외한 폭죽 더미 하나를 고른다 -> 마지막에는 무조건 양쪽 끝 더미만 남게된다.
left = arr[0]
right = arr[-1]
for _ in range(N-3):
    if left > right : left -= 1
    else : right -= 1
left-=1
right-=1

print(max(left,right))