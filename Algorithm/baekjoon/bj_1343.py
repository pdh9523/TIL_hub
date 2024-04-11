a = input()

list_a = a.split(".")
test_case = []
for i in list_a :
    if i == "" :
        test_case.append(".")
    else :
        test_case.append(i.count("X"))

output = ""

for element in test_case :
    if element == "." :
        output+= "."
        continue
    elif element % 2 == 1 :
        output = -1
        break
    else :
        while element > 0 :
            if element >= 4 :
                element -= 4
                output += "AAAA"
            if element == 2 :
                element -= 2
                output += "BB"
        output+="."

if output == -1 :
    print(output)
else :
    print(output[:-1])