# ## 괄호 조건이 중첩 괄호 사용 불가
# ### 코드 다시 짜야함 ###


# def backtrack(result,idx = 0):
#     global max_value, calc
#     if idx == lenc :
#         max_value = max(max_value,result[0])
    
#     target = len(calc)
#     for i in range(target):
#         tmp = eval(f'{result[i]}{calc[i]}{result[i+1]}')
#         print(tmp, result)
#         temp1 = result[:]
#         temp2 = calc[:]
#         result.pop(i)
#         result.pop(i)
#         calc.pop(i)
#         result.insert(i,tmp)
#         backtrack(result,idx+1)
#         result = temp1
#         calc = temp2
# N = int(input())

# char = list(input())

# nums = [int(char.pop(0))]
# calc = [ ]
# for i in range(0,N-1,2):
#     calc.append(char[i])
#     nums.append(int(char[i+1]))
# lenc = len(calc)
# max_value = -float('inf')
# backtrack(nums)

# print(max_value)