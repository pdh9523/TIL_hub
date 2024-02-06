def ispan(arr,cut) : # 입력된 길이에 의한 회문 비교
    count = 0
    for ele in arr :
        for idx in range(len(ele)-cut+1) :
            text = ele[idx:idx+cut] # 슬라이싱으로 떼어내고
            if text == text[::-1] : # 뒤집어서 같은지 비교합니다.
                count += 1 # 같다면, 카운트를 올립니다. 
    return count # 모두 비교하여 총 카운트를 반환합니다.

for idx in range(10) :
    a = int(input()) # 함수의 cut에 들어갈 숫자
    test_case = [input() for _ in range(8)] # 2차원 리스트 
    tilted_case = ["".join(char) for char in zip(*test_case)] # 90도 돌린 2차원 리스트
    print(f"#{idx+1} {ispan(test_case, a) + ispan(tilted_case, a)}") 