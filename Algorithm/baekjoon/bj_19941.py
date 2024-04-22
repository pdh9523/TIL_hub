import sys
input = sys.stdin.readline
 
N, K = map(int, input().split())
arr = list(input().strip())

ans = 0 
for i in range(N):
    if arr[i] == 'H':
        for j in range(i-K, i+K + 1):
            if 0 <= j < N: 
                if arr[j] == 'P':
                    arr[j] = '-'
                    ans += 1
                    break
print(ans)