a = int(input()) #약수 개수
test_case = list(map(int,input().split()))
test_case.sort()

if a % 2 == 1 :
    print((test_case[a//2])**2)
else :
    print(test_case[0]*test_case[-1])