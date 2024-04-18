sosu = dict()
table = [True] * 10001
table[0] = table[1] = False

for i in range(2,10001):
    if table[i] :
        sosu[i] = True
        tmp = i
        while tmp+i < 10001 :
            tmp += i
            table[tmp] = False
        
for _ in range(int(input())):
    
    num = int(input())

    for j in range(num//2, 1,-1) :
        if sosu.get(j) and sosu.get(num-j) :
            print(j, num-j)
            break