alphabet = input()

for i in range(len(alphabet)) :
    if alphabet[i].isupper() :
        print(ord(alphabet[i])-64,end = " ")
    else : 
        print(ord(alphabet[i])-96,end = " ")

