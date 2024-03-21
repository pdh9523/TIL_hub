num = int(input())                                          # 목표 숫자

broken = int(input())                                       # 부서진 버튼 개수
button = []                                                 # button : 부서진 버튼
if broken :                                                 # 0 일 경우 button 리스트가 정의되지 않을 수 있음
    button = input().split()

min_value = abs(100-num)                                    # 최소치 (단순히 위아래로 올린 경우)

for i in range(1000000):                                    # 전수조사

    '''
    99999까지인 이유 : 50만이 최대 타겟 채널인데, 9를 제외한 모든 버튼이 고장난 경우
    1000000번에서 내려가는 경우를 상정해야함 
    이를 위해 1000000 까지 전수조사를 진행

    100만개를 집어넣어도, 일반적으로 1초에 2천만회의 연산이 가능하고
    추가적인 조건이 달린다고 하더라도 시간 제한 2초는 허용 범위 내라고 판단.
    '''
    
    for char in str(i):                                     # 버튼이 고장나지 않은 경우 갈 수 있는 숫자만 탐색
        if char in button :
            break                                           # 탐색하는 숫자의 버튼이 고장났으면 break

    else:                                                   # 버튼을 눌러 갈 수 있는 곳이면
        min_value = min(min_value, abs(num-i)+len(str(i)))  # 버튼 클릭 회수와 현재 저장된 값 중 낮은 값 채택
# 출력        
print(min_value)num = int(input())                                          # 목표 숫자

broken = int(input())                                       # 부서진 버튼 개수
button = []                                                 # button : 부서진 버튼
if broken :                                                 # 0 일 경우 button 리스트가 정의되지 않을 수 있음
    button = input().split()

min_value = abs(100-num)                                    # 최소치 (단순히 위아래로 올린 경우)

for i in range(1000000):                                    # 전수조사

    '''
    99999까지인 이유 : 50만이 최대 타겟 채널인데, 9를 제외한 모든 버튼이 고장난 경우
    1000000번에서 내려가는 경우를 상정해야함 
    이를 위해 1000000 까지 전수조사를 진행

    100만개를 집어넣어도, 일반적으로 1초에 2천만회의 연산이 가능하고
    추가적인 조건이 달린다고 하더라도 시간 제한 2초는 허용 범위 내라고 판단.
    '''

    
    for char in str(i):                                     # 버튼이 고장나지 않은 경우 갈 수 있는 숫자만 탐색
        if char in button :
            break                                           # 탐색하는 숫자의 버튼이 고장났으면 break

    else:                                                   # 버튼을 눌러 갈 수 있는 곳이면
        min_value = min(min_value, abs(num-i)+len(str(i)))  # 버튼 클릭 회수와 현재 저장된 값 중 낮은 값 채택
# 출력        
print(min_value)