t = int(input())

paper = [50000,10000,5000,1000,500,100,50,10]

for i in range(t) :
    paper_bin = [0,0,0,0,0,0,0,0]
    cash = int(input())
    c = 0 
    cnt = 0
    while c != 8:
        if cash >= paper[c] :
            cash -= paper[c]
            cnt += 1
        else :
            paper_bin[c] = cnt
            c+=1
            cnt = 0
    print(f"#{i+1}")
    print(*paper_bin)