test_dict = {
    'black' : '0',
    'brown' : '1',
    'red' : '2',
    'orange' : '3',
    'yellow' : '4',
    'green' : '5',
    'blue' : '6',
    'violet' : '7',
    'grey' : '8',
    'white' : '9'
}
output = ''
for i in range(2) :
    a = input()
    output += test_dict[a]
b = input() 
output += '0' * int(test_dict[b])

print(int(output))