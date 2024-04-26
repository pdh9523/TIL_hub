from itertools import combinations
import time
a= time.time()
b= len(list(combinations(range(2500),2)))

print(time.time()-a)