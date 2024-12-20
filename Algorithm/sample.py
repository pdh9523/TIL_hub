cache = dict()

def memo(f):
	def wrapper(*args):
		if args not in cache: 
			cache[args] = f(*args)
		return cache[args]
	
	return wrapper

@memo
def fibonacci(n):
	return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))