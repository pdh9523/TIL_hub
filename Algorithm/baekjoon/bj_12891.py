S,P = map(int,input().split())
text = input()
dr = {'A':0, 'C':1, 'G':2, 'T':3}
require = list(map(lambda x: -int(x), input().split()))

left = 0
right = P 

ans = 0
for i in text[left:right]:
    require[dr[i]] += 1

while S >= right :
    if all(num >= 0 for num in require): 
        ans+=1
    require[dr[text[left]]] -= 1

    left += 1
    right += 1
    if S > right-1:
        require[dr[text[right-1]]] += 1

print(ans)