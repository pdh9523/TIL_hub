import sys

test_set = set()

t = int(input())

for _ in range(t) :
    order = sys.stdin.readline().strip("\n")
    if order == "all" :
        test_set = set(range(1,21))
    elif order == "empty":
        test_set = set()
    else :    
        order, num = order.split()
        num = int(num)
        if order == "add" :
            test_set.add(num)
        elif order == "remove" :
            if num in test_set :
                test_set.remove(num)
        elif order == "check" :
            if num in test_set : 
                print(1)
            else :
                print(0)
        elif order == "toggle" :
            if num in test_set :
                test_set.remove(num)
            else :
                test_set.add(num)
