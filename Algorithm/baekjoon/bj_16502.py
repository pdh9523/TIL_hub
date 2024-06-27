def cal(char):
    return ord(char)-ord("A")

N,M = int(input()), int(input())
graph = [[] for _ in range(4)]

for _ in range(M):
    s,e,p = input().split()
    graph[cal(s)].append((cal(e),float(p)))

ans = [25] * 4
for _ in range(N):
    tmp = [0] * 4
    for i in range(4):
        for k,v in graph[i] : tmp[k] += ans[i]*v
    ans = tmp
print(*ans, sep="\n")