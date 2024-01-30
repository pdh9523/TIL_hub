a = [1,2,2,2,1,1,2,1,1,1]
k = 4
def bus(arr, k) :
    new_list = []
    for ele in range(len(arr)) :
        idx = 0
        while arr :
            if sum(arr[ele:idx]) < k :
                idx += 1
            if sum(arr[ele:idx]) > k :
                idx -= 1
                new_list.append(sum(arr[ele:idx]))
                for i in range(idx) :
                    arr.pop(0)
            if sum(arr[ele:idx]) == k :
                new_list.append(sum(arr[ele:idx]))
                for i in range(idx) :
                    arr.pop(0)
    return new_list

print(bus(a,k))
