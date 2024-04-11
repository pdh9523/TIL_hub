test_list = list(range(1,int(input())+1))

stack = []


while test_list :
    if test_list :
        stack.append(test_list.pop())
    if test_list :
        test_list.append(test_list.pop(0))

print(*stack)