def quick(start, end) :
    # 언제까지 조사할 것인가?
    # 스택에 값이 있는 동안
    stack = [(start,end)]
    while stack :
        start, end = stack.pop()
        if start < end :    # 조사 범위가 꼬이지 않았다면 (피봇으로 인해 분할될 수 있음)
            pivot_idx = partition(start,end)    # 파티션을 통해 피봇을 기준으로 구간을 나눠주고
            stack.append((start,pivot_idx-1))   # 다음 처리할 값에 대해 조사한다
            stack.append((pivot_idx+1, end))



def partition(start, end) :
    pivot = arr[end]
    i = start - 1
    for j in range(start, end) :
        if arr[j] <= pivot :    # 배열에 들어가있는 값이 피봇보다 크거나 같다면
            i += 1              # 마지막 pivot 위치의 값이 들어가야 할 위치
            arr[i], arr[j] = arr[j], arr[i] # 스왑
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


arr = [3,6,8,10,1,2,1]
N = len(arr)
quick(0,N-1)
print(arr)