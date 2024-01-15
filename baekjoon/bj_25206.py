score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
under = 0
upper = 0
for i in range(20) :
    a = input()
    if a[-1] == "P" :
        pass
    elif a[-1] == "F" :
        under += float(a[-6:-3])
    else : 
        upper += score[a[-2:]]* float(a[-7:-4]) # 평점
        under += float(a[-7:-4]) # 학점
print(upper/under)