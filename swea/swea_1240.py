import sys
sys.stdin = open("1240.txt")

test_dict = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9
}

t = int(input())
for i in range(t):
    check = True
    size, length = map(int,input().split())
    for _ in range(size):
        data = input()
        if check :
            for idx in range(length-55):
                if data[idx:idx+7] in test_dict and data[idx+49:idx+56] in test_dict:
                    code = data[idx:idx+56]
                    check = False
                    break
        # 나머지 부분 또한 input으로 받아야하기 때문에 중간에 input이 담긴 for문을 완전히 벗어날 수 없다.

    # code 를 7개씩 나누기
    key = []
    for idx in range(8):
        key.append(code[7*idx:7*idx+7])
    # 딕셔너리를 기반으로 암호 해석
    result = list(map(lambda x : test_dict.get(x, -1) , key))

    # case 1) 딕셔너리에 저장된 암호가 없다 = 암호가 아니다 - > 0 출력
    if -1 in result :
        print(f"#{i+1} {0}")
    # case 2) 정상적인 경우 - > 암호의 총합 출력
    elif ((3 * sum(result[0::2])) + sum(result[1::2]))%10 == 0 :
        print(f"#{i+1} {sum(result)}")
    # case 3) 암호 검증이 틀린 경우 - > 0 출력
    else :
        print(f"#{i+1} {0}")