t = int(input())

for i in range(t) :
    test_str = input()
    if test_str == test_str[::-1] :
        print(f"#{i+1} 1")
    else :
        print(f"#{i+1} 0")