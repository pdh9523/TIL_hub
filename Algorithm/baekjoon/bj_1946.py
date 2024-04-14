import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = sorted([list(map(int,input().split())) for _ in range(N)])
    # 앞 번호를 기준으로 정렬되어있으니
    cnt = 0
    mini = arr[0][1]
    # 뒷 번호를 기준으로 가장 작은 값부터 순회하면서
    for i in range(N):
        # 뒷번호가 더 작으면 갱신 후 cnt += 1
        if mini >= arr[i][1]:
            mini = arr[i][1]
            cnt += 1
            
    print(cnt)