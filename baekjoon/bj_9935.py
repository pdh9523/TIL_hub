text = input()
target = input()
length = len(target)
stack = []

for char in text :
    stack.append(char)
    if len(stack) >= length :
        for i in range(1,length+1):
            if target[-i] != stack[-i]:
                break
        else :
            for i in range(length):
                stack.pop()
if stack :
    print("".join(stack))
else :
    print("FRULA")