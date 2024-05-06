N = int(input())

hanoi = [[*map(int,input().split())],[],[]]
ans = []
for num in range(N,0,-1):
    for i in range(2):

        if num in hanoi[i]:

            while hanoi[i][-1] != num:
                hanoi[1-i].append(hanoi[i].pop())
                ans.append((i+1, 2-i))

            hanoi[2].append(hanoi[i].pop())
            ans.append((i+1, 3))
print(len(ans))
for a in ans:
    print(*a)
