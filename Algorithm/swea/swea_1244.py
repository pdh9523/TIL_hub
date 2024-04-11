def backtrack(idx=0,result=0):                      # 대 트 래 킹
    if idx == cnt:
        ans.append(result)
        return
    
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            
            num[i], num[j] = num[j], num[i]

            result = int("".join(num))
            if (idx,result) not in visit:
                visit.append((idx,result))
                backtrack(idx+1,result)

            num[i], num[j] = num[j], num[i]
            

for t in range(int(input())):
    num,cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    visit = []
    ans = []

    backtrack()

    print(f"#{t+1} {max(ans)}")