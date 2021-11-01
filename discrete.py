# Create a function that will calculate a factorial of a given number
# factorial(5) will give you 1 * 2 * 3 * 4 * 5
# the parameter will always be positive 
def factorial(num):
	if num == 0:
		return 1
	else:
		answer = 1
		for i in range(1, num+1):
			# answer / i 
			# 1 * 1 = 1
			# 1 * 2  = 2
			# 2 * 3 = 6
			# 6 * 4 = 24
			# 24 * 5 = 120
 			answer *= i
		return answer

print(factorial(5))


# You can also use a built-in function by Python to calculate a given number
# This faction is part of math library, and is called fatorial


import math

answer = math.factorial(6)
print(answer)

# Permutations

#  List Recap

# Create a list that has three items which is 1,2,3,4
lists = [1,2,3,4]

#Bring out the second element of the list - 2
print(lists[1])

# Bring out all the element before the second element = [1]
print(lists[:1])


# Bring out all the element after the second element - [3,4]
print(lists[2:]) 

#List down all the number in the list using loop
# len(lists) => How many items in the list
for i in range(0,len(lists)):
	print(lists[i])

#You will now modify the previous loop,
# for each of the loop, you will list down the left element from the index
# and you will list down the right element from the index
#eg:
# index - 2
# left - [1]
# right - [3,4]


# for i in range(0, len(lists)):
# 	print("index "+str(lists[i]))
# 	print("left "+str(lists[:i]))
# 	print("right "+str(lists[i+1:]))

# You will now create a function from the above instruction by retrieving a list as parameter
# Call it permutation

# def permutation(lists):
# 	for i in range(0, len(lists)):
# 		print("index "+str(lists[i]))
# 		print("left "+str(lists[:i]))
# 		print("right "+str(lists[i+1:]))

# listbaru = [1,5,11,8,20,11]
# print(permutation(listbaru))

# Inside the above function, you will create 2 lists, the first one is indexArr
# Second one is what we call remaining
# for example , If list is [1,2,3,4] , i = 2, index = [2], remaining = [1,3,4]
# How would you do it?

def permutation(lists):
	for i in range(0, len(lists)):
		indexArray = [lists[i]]
		remaining = lists[:i] + lists[i+1:]
		print("index")
		print(indexArray)
		print("remaining")
		print(remaining)

listbaru = [1,2,3,4]
print(permutation(listbaru))

#You will repeat the previous function by calling inside remaining.. and list down all the lists and remaining


def permutation(lists):

	# If it is an empty array, there is no permutation

	if len(lists) == 0:
		return []

	# Bring out the bold item from the google drive
	if len(lists) == 1:
		return [lists]

	# This is where answer will be stored:
	answer = []

	for i in range(0, len(lists)):
		indexArray = [lists[i]]
		remaining = lists[:i] + lists[i+1:]

		for p in permutation(remaining):
			answer.append(indexArray+p)
	return answer

listbaru = [1,2,3]
# print(permutation(listbaru))

# In Python, there is a module that is called itertools
# that can be used for all items related to permutations and combinatons

from itertools import permutations

lists = [1,2,3,4]

newLists = permutation(lists)
# print(newLists)


from itertools import combinations

lists = [1,2,3,4]
# Generate a combination from list, where each of the sublist will have 2 eleements
combinaLists = combinations(lists,2)

# Go through the list and show all the items in the list
for item in combinaLists:
	print(item)


#Probability
#Random function in Pyton



# Function random() in Python will generate a random number between 0-1



# Add logic to this code, so that it will return Head or tail (50/50)



# Create a function coin toss so that you can call it later xxx number of times
# Call this function tossCoint

import random

def coin_toss():
	toss = random.random()
	if toss < 0.5:
		return "Head"
	else:
		return "Toss"

# Call this function 100 times




# userInfo = {"name":"Muzaffar","location":"Bangi"}
# print(userInfo)
# print(userInfo["name"])

# Now you will add the results in a Dictionary and you will modify the previous function so that 
# it will stores how many times head/tail appears in a dictionary

results = {"head":0,"tail":0}

for i in range(0,100000):
	result = coin_toss()
	if result == "Head":
		results["head"] = results["head"]+1
	else:
		results["tail"] = results["tail"]+1

print(results)

# What is the probability for head and tail to appear?? 57/100 43/ 100
# Every person will get different result

## Increase the number of coin toss from 10, 20, 50, 100, 1000, 10 000, 100 000
## See the result and calculate the probability for each time

# 10 == HEad = 6/10 tail = 4/10
# 20  == head = 8/20 tail = 12/20
# 50 = head 24/50  tail 26/50 = 12/15
# 100 == HEad = 39/100 tail = 61/100
# 1000 == HEad = 0.483 tail = 0.517
# 10 000 = 0.4983 tail = 0.5017
# 100 000 = 0.49677 tail = 0.50323


# Dadu 
results = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}

def launch_dice():
	dice = random.random()
	if dice < 1/6:
		return "1"
	elif dice < 1/3:
		return "2"

	elif dice < 0.5:
		return "3"

	elif dice < 4/6:
		return "4"


	elif dice < 5/6:
		return "5"

	else:
		return "6"

for i in range(0,100000):
	result = launch_dice()
	if result == "1":
		results["1"] = results["1"]+1
	elif result == "2":
		results["2"] = results["2"]+1
	elif result == "3":
		results["3"] = results["3"]+1
	elif result == "4":
		results["4"] = results["4"]+1
	elif result == "5":
		results["5"] = results["5"]+1
	else:
		results["6"] = results["6"]+1

print(results)

# THe more you test, the closer it is to the actual probability

# THis can also be verified with the binomial function in python
# Binomial function is part of random function from numpy module

from numpy import random

x = random.binomial(n=10,p=0.5,size=100)

print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size = 10000), hist=True, kde=False)
plt.show()



