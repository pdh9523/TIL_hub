def quick(lst) :                # idx 조절이 아닌 lst 자체를 조절
    if len(lst) <= 1:           # 정렬대상을 분할해 나가다가
        return lst              # 더 이상 분할할 수 없는 상태가 되면, 해당 리스트 반환
    else :
        pivot = lst[0]          # 퀵소트의 pivot 위치는 아무 대상이어도 상관없다. (교재는 중앙)
        less_than = [x for x in lst[1:] if x <= pivot]          # arr의 피봇+1 (1) 부터 끝까지의 원소 중 pivot 보다 작거나 같은 원소
        gret_than = [x for x in lst[1:] if x > pivot]           # arr의 피봇+1 (1) 부터 끝까지의 원소 중 pivot 보다 큰 원소
        return quick(less_than) + [pivot] + quick(gret_than)    # 피봇으로 나눠진 두 리스트를 다시 조사한다



arr = [3,6,8,10,1,2,1]
quick_arr = quick(arr)
print(quick_arr)