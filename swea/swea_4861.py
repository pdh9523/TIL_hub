def ispan(arr,cut) : # 입력된 길이에 의한 회문 비교
    for ele in arr :
        for idx in range(len(ele)-cut+1) :
            text = ele[idx:idx+cut] # 슬라이싱으로 떼어내고
            if text == text[::-1] : # 뒤집어서 같은지 비교합니다.
                return text # 모두 비교하여 회문이 있는 경우 반환합니다.
    else :
        return "" # 없으면 ""를 반환합니다.(나중에 회전 리스트와 합치려고)
t = int(input())


for index in range(t) :
    a,b = map(int,input().split()) # a는 배열의 길이, b는 cut에 들어갈 변수입니다.
    test_case = [list(input()) for _ in range(a)] # 2차원 리스트 
    # 회전시킬거라 일단 list로 하나씩 분리했습니다.
    tilted_case = [] # 회전된 리스트 할당
    for i in range(a) :
        rem = []
        for j in range(a) :
            rem.append(test_case[j][i]) # 회전해서 담고
        tilted_case.append("".join(rem)) # join메서드로 합체
    for idx in range(len(test_case)) :
        test_case[idx] = "".join(test_case[idx]) # 원본도 join으로 합체

    print(f"#{index+1} {ispan(test_case, b)+ispan(tilted_case, b)}")