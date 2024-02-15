arr = list(range(1,11,2))
N = len(arr)

'''
K = 탐색 대상이 된 원소 번호
result = 최종 결과값
cnt = 부분 집합의 합이 몇이냐
'''

def powerset(K, result, target, cnt=0) :
    # 언제까지 조사할 것인가
    if cnt > target :
        return
    
    if K == N : # 모든 원소에 대해 조사를 마쳤다면, 
        # 다음 조건 : 부분집합의 합이 cnt인 경우
        if cnt == target :
            print(result)
            return
    else : # 조사할 대상이 남은 경우
        # K를 사용했는가?
        # K번째 값을 사용한 경우
        powerset(K+1, result + [arr[K]], target, cnt + arr[K])
        # 사용하지 않은 경우
        powerset(K+1, result, target, cnt)

powerset(0, [], 11)