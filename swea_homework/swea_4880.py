def rsp(per1, per2) :
    if per1[1] == per2[1] :
        if per1[0] < per2[0] :  # 같은 것을 내면 숫자가 작은 쪽으로
            return per1
        else :
            return per2
    elif per1[1] == 1 :
        if per2[1] == 2: 
            return per2
        elif per2[1] == 3 :
            return per1
    elif per1[1] == 2 :
        if per2[1] == 3 :
            return per2
        elif per2[1] == 1 :
            return per1
    elif per1[1] == 3:
        if per2[1] == 1 :
            return per2
        elif per2[1] == 2 :
            return per1
# 1 가위 2 바위 3 보

def conquer(lst) :
    start = 1
    end = len(lst)

    if len(lst) == 2 :              # 가위바위보 성립 조건 : 1:1이 성립되는 경우 (길이가 2인 리스트인 경우 대결 가능)
        return [rsp(lst[0],lst[1])]
    
    elif len(lst) == 1 :            # 수렴 조건 : 마지막에 입력 받은 리스트 내부의 요소 중 하나의 결과만 가진 리스트를 반환
        return lst

    else :
        front = [x for x in lst[:(start+end)//2]]   #앞
        back = [x for x in lst[(start+end)//2:]]    #뒤
        return conquer(conquer(front) + conquer(back))    #나누고 합치는 작업을 반복

##########

t = int(input())

for i in range(t) :
    test_range = int(input())
    test_list = list(enumerate(list(map(int,input().split()))))     # enumerate를 통해 tuple로 작업

    print(f"#{i+1} {conquer(test_list)[0][0]+1}") # list(tuple(idx, value)) 의 형태이기 때문에 이중으로 인덱싱을 하고, 인덱스와의 차이를 보정하기 위해 +1 시행