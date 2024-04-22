def recur(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)
    
    if memo.get((a,b,c)):                # 메모이제이션 : 미리 계산된 값을 바로 들고온다. 
        return memo[(a,b,c)]
    
    if a < b < c:
        memo[(a,b,c)] =  recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
        return memo[(a,b,c)]
    
    memo[(a,b,c)]= recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
    return memo[(a,b,c)]

memo = dict()

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1 : break
    print(f'w({a}, {b}, {c}) = {recur(a,b,c)}')