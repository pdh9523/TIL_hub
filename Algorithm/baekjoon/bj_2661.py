def check(num):
    for idx in range(1, len(num)//2+1):
        if num[-idx:] == num[-idx*2:-idx]:
            return False
    return True

def backtrack(idx, num=""):
    if not idx: exit(print(num))

    for i in '123':
        if check(num+i): backtrack(idx-1,num+i)
    
backtrack(int(input()))