a,b = input().split() # 뒤집을거니까 숫자로 안받음

a = a[::-1] # 문자열 뒤집기
b = b[::-1]

if int(a) > int(b) : # 뒤집은 후 정수변환해서 비교 
    print(a)
else :
    print(b)