aeiou = ['a','e','i','o','u']
def backtrack(idx=0, result=''):
    if idx == L :
        check = False
        tmp = 0
        for i in result :
            if i in aeiou :
                check = True
            else :
                tmp += 1
            if check and tmp >= 2 :
                print(result)
                return
        return

    for i in arr :
        if i not in result :
            if not result or result[-1] < i :
                backtrack(idx+1, result+i)


L,C = map(int,input().split())
arr = sorted(input().split())
ans = []
backtrack()