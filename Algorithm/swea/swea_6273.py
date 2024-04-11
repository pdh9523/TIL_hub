a = [(90,80), (85,75), (90,100)]
tag = 0
for i in a :
    tag +=1
    sum_a = sum(i)
    mid = sum(i) / 2
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(tag,sum_a,mid))