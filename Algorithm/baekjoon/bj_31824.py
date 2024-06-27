def query(data, s):
    ans = ""
    for i in range(len(s)):
        for j in range(i,len(s)):   # 문자열은 최대 100자 이기 때문에 N**2 이라도 10000개
            char = s[i:j+1]         # 문자열을 슬라이싱한 후, 키값과 비교
            if char in data : ans += data[char]
    return ans if ans else -1

N,M = map(int,input().split())

data = dict()
for _ in range(N):
    k, v = input().split()
    data[k] = v

for _ in range(M) : print(query(data, input()))