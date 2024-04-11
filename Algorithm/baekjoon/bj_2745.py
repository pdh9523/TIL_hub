a,b = input().split()
# a = 구문
# b = 진수
output = 0
b = int(b)
for i in range(len(a)) :
    rem = 0
    if a[i] in ['1','2','3','4','5','6','7','8','9','0'] :
        rem = int(a[i])
    else : 
        rem = ord(a[i]) - 55
    output += rem * (b ** (len(a)-i-1))

print(output)