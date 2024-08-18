def backtrack(idx=0, result="", visit=0):
    if idx==len(S):
        data.add(result)
        return
    
    for i in range(len(S)):
        if visit & 1<<i: continue
        if result and result[-1] == S[i]: continue
        backtrack(idx+1, result+S[i], visit|1<<i)

S = input()
data=set()
backtrack()
print(len(data))
