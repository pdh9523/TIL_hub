def pal (n) : # 회문 함수
    for i in range(len(n)) :
        if n[i] != n[len(n)-1-i] :
            break
    else : 
        return True

t = int(input())
for i in range(t) :
    text_list = []
    n,m = map(int,input().split())
    for j in range(n) :
        text_list.append(input())
# 여기까지 준비과정 
        
    for k in text_list :
        