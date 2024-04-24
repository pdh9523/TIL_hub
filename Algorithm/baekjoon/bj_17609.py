for _ in range(int(input())):

    text = input()

    left, right = 0, len(text)-1
    check = 2
    while left < right : 

        if text[left]==text[right]:
            left+=1
            right-=1
            continue
        if check == 2 and text[left+1] == text[right]:
            check = 1
            left += 2
            right -= 1
            continue

        if check == 2 and text[left] == text[right-1]:
            check = 1
            left += 1
            right -= 2
            continue
        check = 0
        print(2)
        break

    if check==1:
        print(1)
    elif check==2:
        print(0)

        