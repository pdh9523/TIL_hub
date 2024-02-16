import sys
t,idx = map(int,input().split())

test_list = list(map(int,sys.stdin.readline().strip("\n").split()))
for i in range(1,t) :
    test_list[i] += test_list[i-1]
test_list.insert(0,0)

for _ in range(idx) :
    start,end = map(int,sys.stdin.readline().strip("\n").split())
    print(test_list[end] - test_list[start-1])