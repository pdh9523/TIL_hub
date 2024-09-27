def cal(ans, order, tmp):
    try:
        if order == "/":
            tmp = int(tmp)
            if ans/tmp < 0:
                if ans % tmp:
                    return ans // tmp + 1
            return ans // tmp
        else:
            return int(eval(str(ans)+order+tmp))
    except:
        exit(print("Madness!"))

cmd = {
    "ONE": "1",
    "TWO": "2",
    "THREE": "3",
    "FOUR": "4",
    "FIVE": "5",
    "SIX": "6",
    "SEVEN": "7",
    "EIGHT": "8",
    "NINE": "9",
    "ZERO": "0",
    "x": "*"
}

S = input()
for num in cmd:
    S = S.replace(num, cmd[num])

ans = 0
tmp = ""
order = "+"
for char in S:
    if char.isnumeric():
        tmp += char
    else:
        ans = cal(ans, order, tmp)
        tmp = ""
        order = char
        
ans = str(ans)
for num in cmd:
    ans = ans.replace(cmd[num], num)

print(S.replace("*", "x"))
print(ans)