# 순서대로 잘 울고 있는지에 대한 함수 정의
def check():
    return list(visit.values()) != sorted(list(visit.values()), reverse=True)

# 입력
text = input()
visit = dict(zip("quack",[0]*5))


ans = 0
# 문자열을 순회하면서
for i in range(len(text)):
    # 방문 여부를 더해주고
    visit[text[i]] += 1
    # 순서대로 잘 울지 않았으면
    if check():
        # ans를 -1로 덮고 순회 종료
        ans = -1 
        break
    # 모든 밸류가 1이상이면
    if all(visit.values()):
        # 지금 누적된 q 의 값이 지금 같이 울고 있는 오리 수
        ans = max(visit["q"], ans)
        # 다 울었으니까 오리빼주기
        for i in visit:
            visit[i] -= 1

# 순회 후 울음이 남아 있는 경우
if sum(visit.values()):
    # 잘못됐으니 ans를 -1로 덮고 순회 종료
    ans=-1

#출력
print(ans)