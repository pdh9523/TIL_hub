s = input()
ans = length = len(s)
caps = False
for i in range(length):
    if s[i].isupper() and not caps:
        caps = True
        ans += 1
        if i < length-1:
            if s[i+1].islower():
                caps = False

    elif caps and s[i].islower():
        ans += 1
        caps = False
        if i < length-1:
            if s[i+1].isupper():
                caps = True
print(ans)