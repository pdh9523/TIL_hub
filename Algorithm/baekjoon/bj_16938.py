def backtrack(idx=0, visit=[], summ=0, min_visit=float('inf'),max_visit=0):
    global ans
    
    if len(visit)>=2:
        if L<= summ <= R and max_visit-min_visit >= X:
            ans.setdefault(tuple(visit),1)
    if idx == N :
        return
    
    backtrack(idx+1, visit+[idx], summ+arr[idx], min(min_visit,arr[idx]), max(max_visit,arr[idx]))
    backtrack(idx+1, visit, summ, min_visit, max_visit)


N,L,R,X = map(int,input().split())
arr = [*map(int,input().split())]
ans = dict()
backtrack()
print(sum(ans.values()))