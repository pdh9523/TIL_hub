# a,b,v = map(int,input().split())

# length = 0
# day = 0

# while v > length :
#     day += 1
#     length += a
#     if length >= v :
#         break
#     length -= b

# print(day)
# 위의 코드 처럼 생각대로 처리하면 시간 초과 발생

import math

a,b,v = map(int,input().split())

day_length = a - b #하루에 a-b씩 올라감
goal = v - b # 마지막날 a만큼만 올라가면 되니까 b를 빼줌

print(math.ceil(goal/day_length)) # 올림 처리