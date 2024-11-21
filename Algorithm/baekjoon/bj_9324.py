import sys; input=sys.stdin.readline

def decode(string):
    data = dict()
    check = ""
    for char in string:
        if check:
            if char != check:
                return False
            else:
                check = ""
                continue
        
        data[char] = data.get(char,0)+1
        if data[char] == 3: 
            check = char
            data[char] = 0
    if check:
        return False
    
    return True

for _ in range(int(input())):
    print("OK" if decode(input().strip()) else "FAKE")


    