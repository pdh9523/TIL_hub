from pprint import pprint as print
test_case = [[1,2,3],
             [4,5,6],
             [7,8,9]]
print([list(char) for char in zip(*test_case[::-1])])