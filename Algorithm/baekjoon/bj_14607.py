'''
피자(Large)
반으로 나누는게 최적이다.
'''
def pizza(num):
    if num in data:
        return data[num]    

    if num % 2:
        a,b = num//2, num//2+1
    else:
        a,b = num//2, num//2
    data[num] = pizza(a) + pizza(b) + a*(b)
    

    return data[num]



N = int(input())
data = dict()
data[1] = 0
print(pizza(N))


# 걍 print(sum(range(int(input())))) 이 답이다.