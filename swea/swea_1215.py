def ispan(arr,cut) : # 입력된 길이에 의한 회문 비교
    count = 0
    for ele in arr :
        for idx in range(len(ele)-cut+1) :
            text = ele[idx:idx+cut] # 슬라이싱으로 떼어내고
            if text == text[::-1] : # 뒤집어서 같은지 비교합니다.
                count += 1 # 같다면, 카운트를 올립니다. 
    return count # 모두 비교하여 총 카운트를 반환합니다.

for index in range(10) :
# ㄷㄱㅈ
    a = int(input()) # 함수의 cut에 들어갈 숫자
    test_case = [list(input()) for _ in range(8)] # 2차원 리스트 
    # 회전시킬거라 일단 list로 하나씩 분리했습니다.
    tilted_case = [] # 회전된 리스트 할당
    for i in range(len(test_case[0])) :
        rem = []
        for j in range(8) :
            rem.append(test_case[j][i]) # 회전해서 담고
        tilted_case.append("".join(rem)) # join메서드로 합체
    for idx in range(len(test_case)) :
        test_case[idx] = "".join(test_case[idx]) # 원본도 join으로 합체

    print(f"#{index+1} {ispan(test_case, a)+ispan(tilted_case, a)}")