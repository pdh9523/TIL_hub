N,K = map(int,input().split())

test_list = list(range(1,N+1))
idx = -1 # 시작 인덱스를 -1로 설정
new_list = []
idx+= K #첫 시행은 한번에 바로 ㄱ
new_list.append(test_list.pop(idx))
while test_list : # 리스트가 빌 때까지
    idx+= K-1 # 인덱스를 K만큼 더하는데, 하나씩 빠지니까 인덱스가 -1 씩 밀립니다.
    while idx >= len(test_list) : # 인덱스가 리스트의 길이보다 긴 경우
        idx -= len(test_list) # 그렇지 않을때까지 뺍니다.
    new_list.append(test_list.pop(idx))

new_list = map(str, new_list)
print( "<" , ", ".join(new_list) , ">" , sep="") # 모양 만들기가 너무 힘듭니다.