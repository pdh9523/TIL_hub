import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())
    div = 2
    c = 1
    while a > 1 and b > 1 :
        while a % div == 0 and b % div == 0 :
            a,b = a//div, b//div
            c *= div
        if div >= a or div >= b :
            break
        
        div +=1
    print(a*b*c)