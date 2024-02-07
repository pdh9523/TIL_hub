i, j = map(int,input().split())

test_list = [list(map(int,input().split())) for _ in range(i)]

result = []
for idx in range(i-2) :
    for jdx in range(j-2) :
        filtered_list = []
        for kdx in range(3) :
            filtered_list.extend(test_list[idx+kdx][jdx:jdx+3])
        filtered_list.sort()
        result.append(filtered_list[4])
target = int(input())
count = 0
for element in result :
    if element >= target :
        count += 1
print(count)