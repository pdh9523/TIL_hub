a = list(input())
output = ""
for char in a :
    if char.islower() :
        output += char.upper()
    elif char.isupper() :
        output += char.lower()
print(output)