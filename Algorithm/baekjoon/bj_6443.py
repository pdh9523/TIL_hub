import sys
input = sys.stdin.readline

def backtrack(idx=0, result=""):
    # 백트래킹 종료 조건
    if idx==len(s):
        return print(result)
    
    for i in data:
        # 데이터가 남아있다면
        if data[i]:
            data[i] -=1
            # result에 더하기
            backtrack(idx+1, result+i)
            data[i] +=1

for _ in range(int(input())):
    s = sorted(input().strip())
    # 중복 제거 및 개수 계산을 위한 딕셔너리 활용
    data = dict()
    for char in s:
        data[char] = data.get(char,0)+1
    backtrack()