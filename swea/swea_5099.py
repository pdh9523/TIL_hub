import sys
sys.stdin = open("5099.txt")

t = int(input())

for i in range(t) :
    size, pizza = map(int,input().split())
    
    ready = list(enumerate(map(int,input().split())))  # 대기방
    ready = list(map(lambda x : (x[0]+1,x[1]), ready))
    fire = list()  # 화덕
    for _ in range(size) :
        fire.append(ready.pop(0))
    
    while len(fire) != 0 :
    
        pizza = fire.pop(0)     # 빼서 확인

        if pizza[1] != 0 :                               # 피자 확인 시 반으로 나눠짐
            fire.append((pizza[0], pizza[1]//2))    # 튜플로 계속 받음

        else :
            if len(ready) > 0 :
                fire.insert(0, ready.pop(0))    # 피자가 빠지면 그자리에 새 피자 넣기

    print(f"#{i+1} {pizza[0]}")