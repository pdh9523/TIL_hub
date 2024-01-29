rot = int(input())
for i in range(rot):
    a = input()

    # a[0,1,2,3] = 년 / a[4,5] = 월 / a[6,7] =일
    year = a[0:4]
    month = int(a[4]+a[5]) 
    day = int(a[6]+a[7])
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
