N = int(input())
text = input()
ans = 0
for i in range(N):
    ans += (ord(text[i])-ord('a')+1) * 31**i
print(ans%1234567891)