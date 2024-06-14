def isprime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

def solution(n, k):
    answer = 0
    data = ""
    if n == 0:
        return 0
    while n>0:
        data = str(n%k) + data
        n //= k
    number = data.split("0")
    print(number)
    for num in number :
        if num and isprime(int(num)):
            answer += 1
    
    return answer