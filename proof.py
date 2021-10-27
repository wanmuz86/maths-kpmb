n = 5

answer = 0
# Sequence / Jujukan
for i in range(1, n+1):
	answer += i

answer2 = n*(n+1)/2 

print(answer == answer2)

# Using the first principle.. let say that for 1 iteration it takes 1s..
# If n = 1000, then it will take 1000 s
# THis code will run 1000 times, we call it O(n) in programming

# For the second code, there is no repetiotion, if the number is 1000,
# THe code will run only 1 time, we call this O(1) in programming

#The second is more  powerful to run in programming