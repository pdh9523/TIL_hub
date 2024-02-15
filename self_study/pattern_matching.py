# 브루트 포스
def brute_force (pattern, target) :
    p_idx = 0   # 패턴 인덱스
    t_idx = 0   # 타겟 인덱스

    while t_idx < len(target) :    # 종료 조건 - 타겟의 길이를 모두 순회
        if pattern[p_idx] != target[t_idx] :    # 타켓의 인덱스와 패턴의 인덱스가 다르면
            p_idx = -1     # 패턴의 인덱스를 0으로 초기화
                    
        t_idx += 1             
        p_idx += 1

        if p_idx == len(pattern) :    # 패턴의 인덱스가 패턴의 길이만큼 (패턴 매칭이 완료되면)
            return True    # True 반환

    return False    # 아닌 경우 False
# KMP
def KMP(pattern, target) :

    def make_lps() :    # lps 배열 만드는 함수 
        lps = [0] * len(pattern)
        for idx in range(1, len(pattern)) :
            if pattern[lps[idx-1]] == pattern[idx] : 
                lps[idx] = lps[idx-1] + 1 
        lps.insert(0,-1)
        return lps

    p_idx = 0
    t_idx = 0
    lps = make_lps()

    while t_idx < len(target) :
        if pattern[p_idx] != target[t_idx] :    # 브루트포스의 같은 경우에서
            p_idx = lps[p_idx]      # 다른 경우 p_idx를 lps의 p_idx로 변경

        t_idx+=1
        p_idx+=1

        if p_idx == len(pattern) :
            return True
    return False

# 보이어-무어
def boyer_moore(pattern, target) :    # 문자열을 뒤에서부터 검색
    lps = {pattern[idx] : len(pattern) -1 -idx for idx in range(len(pattern))}
    p_idx = len(pattern)
    t_idx = 0

    while t_idx <= len(target) - p_idx :
        for idx in range(p_idx-1,-1,-1) :
            if target[t_idx + idx] != pattern[idx] :
                t_idx += lps.get(target[t_idx + idx], len(pattern))
                break
        else :
            return True
    return False




pattern = "aabaacd"
target = "abcdefgaabaacasdaabaacd"
print(brute_force(pattern,target))
print(KMP(pattern,target))
print(boyer_moore(pattern,target))