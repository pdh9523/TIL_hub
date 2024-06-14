import sys
input = sys.stdin.readline

#     도   레   미 파  솔   라  시  
key = [1,0,1,0,1,1,0,1,0,1,0,1]
sound = {0:"C", 2:"D", 4:"E", 5:"F", 7:"G", 9:"A", 11:"B"}

N = int(input())
command = [int(input()) for _ in range(N)]
ans = []
for i in sound:
    tmp=i
    for com in command:
        tmp+=com
        if not key[tmp%12]:
            break
    else :
        ans.append((sound[i%12],sound[tmp%12]))

for i in sorted(ans):
    print(*i)