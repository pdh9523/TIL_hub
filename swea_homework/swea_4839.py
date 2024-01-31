# 이진 탐색을 할건데
# 1. 첫번째 시행 : 1(첫번째 페이지) 400(마지막 페이지) 반띵 -> 200
# 2. 이후 시행 :
# 2-1) 반띵 > 타겟 : 첫번째 페이지는 놔두고 마지막 페이지를 반띵 페이지로 바꿔서 시행
# 2-2) 타겟 > 반띵 : 마지막 페이지는 놔두고 첫번째 페이지를 반띵 페이지로 바꿔서 시행


def binsearch(last, target, first=1) :
    count = 0 # 카운트 설정

    while True : # 종료 조건 : 타겟과 키가 같아지는 경우
        key = int((last+first)/2)
        count += 1
        if key > target :
            last = key
        elif target > key :
            first = key
        elif target == key : 
            return count

t = int(input())        

for i in range(t) :
    book, A, B = map(int,input().split())
    if A > book :
        a_count = 1000
    elif B > book :
        b_count = 1000
    else :
        a_count = binsearch(book,A)
        b_count = binsearch(book,B)
        
        if a_count > b_count :
            print(f"#{i+1} B")
        elif a_count < b_count :
            print(f"#{i+1} A")
        else :
            print(f"#{i+1} 0")