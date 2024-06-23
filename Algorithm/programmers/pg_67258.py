def solution(gems):
    num = len(set(gems))
    res = []

    left = 0
    counter = dict()
    cnt = float('inf')
    for right in range(len(gems)):
        counter[gems[right]] = counter.get(gems[right],0)+1
        while len(counter) == num:
            counter[gems[left]] -= 1

            if counter[gems[left]] == 0:
                counter.pop(gems[left])

            if cnt > right-left:
                cnt = right-left
                res.append([left+1, right+1])

            left += 1
    answer = sorted(res, key = lambda x : x[1]-x[0])[0]
    return answer