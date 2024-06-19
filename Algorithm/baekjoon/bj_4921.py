cnt = 0 
piece = {"1":["4","5"], "3":["4","5"], "4":["2","3"],"5":["8"],"6":["2","3"],"7":["8"],"8":["6","7"]}
while True:
    cnt += 1
    a = input()
    # 입력이 0인 경우
    if a == "0": break
    # 시작이 1, 끝이 2가 아니면 안됨
    if a[0] != "1" or a[-1] != "2": print(f"{cnt}. NOT"); continue
    # 일반적인 경우, piece의 리스트에 담긴 번호만 뒤에 붙을 수 있음
    for i in range(len(a)-1):
        if not (piece.get(a[i]) and a[i+1] in piece[a[i]]):
            print(f"{cnt}. NOT")
            break
    else :
        print(f"{cnt}. VALID")