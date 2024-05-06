N,K = map(int,input().split())

ans = dict()
request = dict()

for _ in range(K):
    student=input()

    if ans.get(student):
        ans.pop(student)
        if request.get(student):
            request.pop(student)
            N+=1
    else :
        if N :
            request[student] = 1
            ans[student] = 1
print(ans)