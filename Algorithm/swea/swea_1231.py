import sys
sys.stdin = open("1231.txt")

def in_order(node):                         # 중위 탐색
    if node !=[] :
        if len(tree[node]) > 0:             # 노드의 잎이 1개 이상인 경우
            in_order(tree[node][0])         # 첫번째 잎으로 재귀 탐색
        print(test_case[node], end="")      # 이파리 다썼으면 문자열 출력
        if len(tree[node]) > 1:             # 노드의 잎이 2개인 경우
            in_order(tree[node][1])         # 두번째 잎으로 재귀 탐색 

for idx in range(1,11):
    N = int(input())
    test_case = [0]
    tree = [[]]
    for _ in range(N):  
        rem = input().split()               # 문자열로 받아서
        rem.pop(0)                          # 앞에 인덱스 숫자 떼고
        test_case.append(rem.pop(0))        # 문자열은 따로 test_case 리스트에 보관
        tree.append(list(map(int,rem)))     # 남은 것이 [] 이거나 [2,4]처럼 자식 노드 인덱스일테니 그것을 모으면 트리 지도
    
    print(f"#{idx}", end =" ")              # 출력 부분에서 꼬였는데, 
    in_order(1)                             # 중위탐색함수가 출력까지 담당하기때문에
    if idx != 10 : print()                  # 인덱스, 함수의 출력, print()를 통한 띄어쓰기 조절 실행