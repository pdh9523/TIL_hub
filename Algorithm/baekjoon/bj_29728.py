from collections import deque

N = int(input())

prime=[True]*(N+1)
prime[0] = False
prime[1] = False
for i in range(2,N+1):
    if prime[i] :
        tmp = i*i
        while tmp <= N:
            prime[tmp]=False
            tmp += i


res = deque([])
B,S = 0,0
dr = True # True : 오른쪽 지우기, False : 왼쪽 지우기
for i in range(1,N+1):

    idx = -1 if dr else 0

    if prime[i]:
        if res[idx]=="B": 
            res[idx] ="S"
            B -= 1

        if dr : 
            res.append("S")

        else : 
            res.appendleft("S")
        S+=1

        dr = not dr
        
    else :
        B += 1
        if dr :
            res.append("B")
        else :
            res.appendleft("B")
            

print(B,S)