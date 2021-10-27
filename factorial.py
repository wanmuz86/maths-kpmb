# Create a function to calculate factorial, for example
# factorial(5) = 1 x 2 x 3 x 4 x 5 = 120
# without recursion
def factorial(number):
	answer = 1;
	if (number == 0):
		return 1
	else:
		for n in range(1,number+1):
			answer = answer * n
		return answer
print(factorial(5))

# with recursion
# 1) We declare a stopper.. f(0) = 1
# 2) We declare the function by calling previous function

def factorial_recursive(number):
	if number == 0:
		return 1
	else:
		return number * factorial_recursive(number-1)
print(factorial_recursive(4))
