
#Theorem of proof.. number theory (Proof - Discrete Math)
# Programatically, list down all the prime number from 2 - 100
# 1) Create a function to check if a number is prime or not
#  -- A prime number is a number that is only divisible by itself and 1
#  --- A prime number is a number that is not divisible by __________ (all number between 1 and itself)
# ---- Build the function programatically

# # Let say if the number is 22
# def is_prime(number):
# 	# Dari 2 hingga 22 (n
# 	for n in range(2,number):
# 		# Jika nombor tersebut boleh dibahagi dengan n
# 		if (number % n == 0):
# 			# Nombor itu bukan prime number
# 			return False
# 	#Jika nombor tersebut tidak boleh dibahagi antara 2 hingga 22
# 	# Nombor tersebut adalah prime number
# 	return True

# for n in range(2,100):
# 	if is_prime(n) == True:
# 		print(n)


# 1) Proof mathematically that a number is a prime number ..
# 2) Build a code to proof that a number is a prime number, 
#calculate it's effectiveness (Big O Notation)
# 3) Have you eliminate all the even number? 
#Improve the code and calculate it's effectiveness
# 4) Use number theory ( A number is a prime number if it is divisible by all the number between 2 and it's square root(n) )
# Calculate it effectiveness - O(log(n)) - > more effective

import math

# Let say number is 97
def is_prime(number):
	# Dari 2 hingga (9) - Theorem of number.. [Sequence]
	for n in range(2,math.ceil(math.sqrt(number))):
		# Jika nombor tersebut boleh dibahagi dengan n
		if (number % n == 0):
			# Nombor itu bukan prime number
			return False
	#Jika nombor tersebut tidak boleh dibahagi antara 2 hingga 22
	# Nombor tersebut adalah prime number
	return True


for n in range(2,100):
	if is_prime(n) == True:
		print(n)
