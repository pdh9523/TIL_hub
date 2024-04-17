N,M = map(int,input().split())

table = [True] * (M+1)

table[0] = table[1] = False

for i in range(2,M+1):

    if table[i] :
        if N <= i <= M :
            print(i)
        tmp = i
        while tmp <= M :
            table[tmp] = False
            tmp += i
        