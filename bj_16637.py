def backtrack(idx, result):
    global ans
    if N == idx :
        ans = max(ans,int(result))

    # 1+2+3+4
    # 괄호를 안쓰는 경우 result : 1, char : 2 + 3 >> join  >> 1*2+3
    if idx+2 <= N :
        backtrack(idx+2, str(eval(''.join([result] + char[idx:idx+2]))))
    # 괄호를 쓰는 경우 result : 1 + , char : (2+3) >> eval 5 >> join >> 1 * 5
    if idx+4 <= N :
        backtrack(idx+4, str(eval(''.join([result, char[idx]] + [str(eval(''.join(char[idx+1:idx+4])))]))))



N = int(input())
char = list(input())

ans = -float('inf')

backtrack(1,char[0])
print(ans)