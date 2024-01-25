import sys
a=int(input())
test_case = set(map(int,sys.stdin.readline().split()))
c=int(input())
compare_case = list(map(int,sys.stdin.readline().split()))

for i in compare_case :
    if ({i} | test_case) - test_case :
        print(0, end=" ")
    else : 
        print(1, end=" ")