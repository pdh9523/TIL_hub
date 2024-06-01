from collections import deque

text = input()

cnt = dict()
for i in text :
    cnt[i] = cnt.get(i,0)+1

# 회문이 만들어지지 않는 조건 :
# 문자열의 길이가 홀수인 경우 : - 한개의 홀수 문자
# 문자열의 길이가 짝수인 경우 : - 0개의 홀수 문자
check = 0
tmp = ""
if sum(cnt.values()) %2 != 0:
    check = 1
for key,value in cnt.items() :
    if value % 2 != 0 :
        tmp = key
        check -= 1

if check != 0 : exit(print("I'm Sorry Hansoo"))

ans = deque()
if tmp :
    ans.append(tmp)
    cnt[tmp] -= 1

for key in sorted(cnt.keys(), reverse=True):
    while cnt[key] :
        ans.append(key)
        ans.appendleft(key)
        cnt[key]-=2
print("".join(ans))