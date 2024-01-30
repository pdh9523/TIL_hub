n,score,p = map(int,input().split())
if n > 0 :
    score_board = list(map(int,input().split()))
else :
    score_board = []
# score가 현재 score_board의 몇번째에 위치하는 지 찾고
# 꼴등이거나 그보다 작으면 -1 출력
# 위치하지 않는다면 그보다 작은 값이 있는지 출력하고, 그 중 가장 큰 값의 위치를 출력

if n < p :
    score_board.append(score)
    score_board.sort(reverse=True)
    print(score_board.index(score)+1)
else :
    if min(score_board) >= score :
        print(-1)
    else : 
        score_board.append(score)
        score_board.sort(reverse=True)
        print(score_board.index(score)+1)
