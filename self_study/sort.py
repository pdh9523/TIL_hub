'''
카운팅 정렬입니다.
'''
arr = [513,356,685,345,234,234,67,678,56,456,345,3453,2,2,24356,234,12]

length = len(arr) 
max_value = max(arr)    # 맥스값

sorted_arr = [0] * length   # 정렬된 숫자를 담을 코드
count = [0] * (max_value+1)     # 카운트를 담을 리스트

for i in range(length) :    # 리스트틀 순회하면서 카운트 세기
    count[arr[i]] +=1

for j in range(1, max_value+1) :    # 카운트를 인덱스에 넣을 수 있도록 정리
    count[j] += count[j-1]

for k in range(length):    # arr의 인덱스를 순회하면서
    count[arr[k]] -= 1      # 숫자를 순차적으로 순회하면서 카운트의 값을 찾고
    sorted_arr[count[arr[k]]] = arr[k]      # count[arr[k]]에 담긴 인덱스를 활용해 위치에 바로 집어넣기

print(sorted_arr)   # 출력

'''
버블 정렬입니다.
'''
arr = [513,356,685,345,234,234,67,678,56,456,345,3453,2,2,24356,234,12]


for i in range(len(arr)-1,-1,-1) :
    for j in range(i) :
        if arr[j+1] < arr[j] : 
            arr[j+1], arr[j] = arr[j], arr[j+1]  # 버블

print(arr)

'''
선택 정렬 입니다.
'''

arr = [513,356,685,345,234,234,67,678,56,456,345,3453,2,2,24356,234,12]

length = len(arr)

for i in range(length-1) : # 어차피 마지막 자료 앞까지만 처리해도 다 정렬된다. 그래서 -1 까지
    min_idx = i # 현재 정렬하려는 인덱스를 정하고
    for j in range(i+1, length) :
        if arr[min_idx] > arr[j] : # 비교하면서 작은 수를 만날때마다 
            min_idx = j # 비교하는 인덱스를 수정한다. (이렇게 최소치를 구함)
    arr[i],arr[min_idx] = arr[min_idx],arr[i] # 최소치와 정렬하려는 값을 서로 바꾼다

print(arr)