s = input()

# 1) 일반적인 경우 (ax+b)
# 2) 1이 붙는 경우 (2x+1)
# 3) 상수항만 있는 경우 (5)
# 4) 상수항이 0인 경우 (0)
# 5) 상수항이 없는 경우 (2x)
check = 0
# 1,2,5
if "x" in s:
    # 1,2
    if "x-" in s:
        a,b = map(int,s.split("x-"))
        check = -1
    elif "x+" in s:
        a,b = map(int,s.split("x+"))
        check = 1
    # 5
    else:
        a,b = int(s[:-1]),0
# 3, 4
else:
    a = 0
    b = int(s)

result = ""
if a == 2:
    result += "xx"
elif a == -2:
    result += "-xx"
elif a == 0:
    pass
else:
    result += f"{a//2}xx"

# 상수항이 있는 경우 
if check:
    if check==1:
        if b == 1:
            result += "+x"
        else:
            result += f"+{b}x"
    else:
        if b == 1:
            result += "-x"
        else:
            result += f"-{b}x"
else:
    if b == 1:
        result += "x"
    elif b == -1:
        result += "-x"
    elif b == 0:
        pass
    else:
        result += f"{b}x"

if result:
    result += "+"
result+= "W"

print(result)