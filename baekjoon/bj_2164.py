from collections import deque

test_list = deque(range(1,int(input())+1))

stack = deque()


while test_list :
    if test_list :
        stack.append(test_list.popleft())
    
    if test_list :
        test_list.append(test_list.popleft())

print(*stack)