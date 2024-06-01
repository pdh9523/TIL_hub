ABC = [300, 60, 10]

num = int(input())

if num % 10 : exit(print(-1))

i = 0

ans = [0,0,0]
while num :
    if num >= ABC[i]:
        num-=ABC[i]
        ans[i]+=1
    else :
        i+=1

print(*ans)