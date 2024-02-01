def ispan(arr) :
    count = 0
    result = 0
    for text in arr :
        for start in range(100) :
            for stop in range(start,100) :
                char = text[start:stop+1] # 슬라이싱 (stop위치 챙겨주기)
                if char == char[::-1] : # 회문 비교
                    count = stop-start+1 # count (stop 뒤로 밀린거 보상해주기)
                    if count > result : # result를 최대값으로 두고, count과 계속 비교
                        result = count 
    return result # 최종적으로 산출된 result 값 반환

for _ in range(10) : 
    t = int(input())
    
### 챗 지피티 방법
# test_case = [input() for _ in range(100)]
# tilted_list = ["".join(char) for char in zip(*test_case)]

    test_list = [list(input()) for _ in range(100)] # 이차원리스트로 받아서 하나씩 회전시킨 후 합칠 예정

    # 회전
    tilted_list = []
    for x in range(100) :
        rem = []
        for y in range(100) :
            rem.append(test_list[y][x]) # 임시 리스트에 테스트 리스트의 각 세로 글자를 받아서
            result_str = "".join(rem) # join 메서드로 합치고
        tilted_list.append(result_str) # 회전 리스트에 추가
    # 테스트 리스트 복구
    for idx in range(100) :
        test_list[idx] = "".join(test_list[idx]) # 회전 리스트를 만든 후 join 메서드로 합침

    print(f"#{t} {max(ispan(tilted_list), ispan(test_list))}")

