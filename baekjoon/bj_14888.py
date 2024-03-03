def backtrack(idx, result):

    global min_value
    global max_value 

    if idx == t-1 :
        min_value = min(min_value, result)
        max_value = max(max_value, result)
    
    for item in range(4) :
        if command[item] > 0 :
            command[item] -= 1
            # 문제에서 제시한 음수 나누기 양수 방식
            if item == 3 and result <0 :
                backtrack(idx+1, -(-result // numbers[idx+1]))
            # 그 외에는 eval 로 계산하기
            else :
                backtrack(idx+1, eval(f"{result}{cmd[item]}{numbers[idx+1]}"))
                # result에 eval로 계산한 값을 넣어 백트래킹
            command[item] += 1





t = int(input())
numbers = list(map(int,input().split()))
command = list(map(int,input().split()))
cmd = ["+","-","*","//"]
min_value = 1000000001                      # min_value : 최소값 / 결과값은 10억 이하
max_value = -1000000001                     # max_value : 최대값 / 결과값은 -10억 이상

backtrack(0,numbers[0])                     # 백트래킹을 하는데, 첫번째 숫자를 result에 넣고 시작

print(max_value)                            
print(min_value)