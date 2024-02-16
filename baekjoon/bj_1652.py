t = int(input())

test_list = [input() for _ in range(t)] # 문자열 리스트
tilted_list = ["".join(char) for char in zip(*test_list)] # 문자열 회전 리스트

# 결과 담을 변수
origin_output = 0
tilt_output = 0

for idx in range(t) :
    test_list[idx] = list(map(len,test_list[idx].split("X"))) # X로 스플릿하고 len으로 숫자로 변경한 값을 리스트로 변환해 담음
    tilted_list[idx] = list(map(len,tilted_list[idx].split("X")))

    for i in test_list[idx] : # 변환된 리스트의 각 값 중 2가 넘는 값이 있으면
        if i >= 2 :
            origin_output += 1 # 결과에 더한다

    for i in tilted_list[idx] :
        if i >= 2 :
            tilt_output += 1
print(origin_output, tilt_output)