# 모음을 반드시 포함
# 모음 / 자음이 3개 이상 연속하면 안됨
# 같은 글자가 2개 이상 연속하면 안됨 (ee, oo 제외)

aeiou = ["a","e","i","o","u"] # 모음 리스트
while True : 
    result = True # 기본 결과값을 True로 둠 (else 적기 귀찮아서)
    test_case = input()
    if test_case == "end" : # 종료 조건 : end 입력
        break

    # 조건 비교
    if len(test_case) == 1: # 한글자인 경우
        if test_case in aeiou : # 그것이 모음이면 
            result = True # 트루
        else : 
            result = False 
    # 일반적인 경우에서
    else :
        for idx in range(len(test_case)-1) : # 다음 글자와 비교를 위해 len -1
            if result == False :
                break
            elif test_case[idx] == test_case[idx+1] : # 뒷글자와 같고
                if test_case[idx] not in ["e","o"] : # 단서조항인 ee 나 oo가 아닌경우
                    result = False # False를 반환
                    break

        for idx in range(len(test_case)-2) : # 3개의 철자를 비교하기 위해 len -2
            if result == False :
                break
            elif test_case[idx] in aeiou and test_case[idx+1] in aeiou and test_case[idx+2] in aeiou : # 3개의 연속하는 모음이 있는가?
                result = False
                break
            elif test_case[idx] not in aeiou and test_case[idx+1] not in aeiou and test_case[idx+2] not in aeiou : # 3개의 연속하는 자음이 있는가?
                result = False
                break
        
        for char in test_case : # 모음이 있는가?
            if result == False :
                break
            elif char in aeiou :
                result = True # 모음 찾았으면 바로 break
                break
        else : # 다 돌아도 모음이 없으면 False
            result = False

    if result == True : 
        print(f"<{test_case}> is acceptable.")
    else :
        print(f"<{test_case}> is not acceptable.")