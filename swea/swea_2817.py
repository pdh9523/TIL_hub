for idx in range(int(input())):
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    result = []
    cnt = 0

    def dfs(depth=0):
        global cnt
        if len(result) > 0 and sum(result) == S:
            cnt += 1
        
        for i in range(depth, N):
            result.append(nums[i])
            dfs(i+1)
            result.pop()

    dfs()
    print(f"#{idx+1} {cnt}")