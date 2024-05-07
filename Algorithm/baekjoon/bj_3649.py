import sys

input = sys.stdin.readline


while True :
    try :
        N = int(input())*10**7
    except : 
        break
    
    M = int(input())

    arr = sorted([int(input()) for _ in range(M)])

    l,r = 0, M-1

    while l < r :
        if arr[l]+arr[r] > N :
            r-=1
        elif arr[l]+arr[r] < N :
            l+=1
        else :
            print('yes',arr[l], arr[r])
            break
    else :
        print('danger')