## 1 2 4 8 16 32 64
test_list = []
for i in range(7) :
    test_list.append(2**i)
count = 0 
t = int(input())
while t > 0 :
    if t >= test_list[-1] :
        t -= test_list[-1] 
        count += 1
    if t < test_list[-1] :
        test_list.pop()
print(count)