# I declare a variable, the name of the variable is a
# The value of  variable a is 10
a = 10
# I declare a variable, the name of the variable is b
# The value of  variable b is 3
b = 3
#Show the value of a and b when you run it
print(a)
print(b)

#Mathematical operation on the number

# I declare a variable, the name of the variable is tambah
# The value of the variable is a + b , 10 + 3 = 13
tambah = a + b;
print(tambah)
tolak = a - b;
print(tolak)
bahagi = a / b;
print(bahagi)
darab = a * b;
print(darab)
modulo = a % b;
print(modulo)
kuasa = a ** b;
print(kuasa)

# Data type pertama = Number (Tiada "" atau '')
# Data type kedua = String (Perlu ada "", atau '')
name = "Muzaffar"
print(name)

# Data type ketiga = Boolean (True / False)
lapar = True
dahaga = False
print(lapar)
print(dahaga)
print (lapar and dahaga)
print(lapar or dahaga)
print(not dahaga)

# Branching with if, if elif and if else
# Create a new variable age, value is 18
# Either ... otherwise (Sama ada, dan lain lain...)
age = 26
if age < 18:
	print("You cannot watch the movie")
else:
	print("You can watch the movie")

# Either this, or that or otherwise
if age < 13:
	print("You cannot watch the movie")
elif age < 18:
	print("Parental guidance required")
else:
	print("You can watch the movie")

## Ticket counter validation
## Under 18 years old and older than 65 years old - discount 50%
## between 19 and 25 - 25 percent off 
## between 26 and 65 normal price
ticketprice = 100
if age < 19 or age > 65:
	print(ticketprice* 0.5)
elif age > 18 and age < 26:
	print(ticketprice * 0.75)
else:
	print(ticketprice)

## Iteration - pengulangan [Sequence/Arimetik]
## for loop, while loops, (for loop..)

# Dari 0 sehingga 10
for n in range(0,10):
# Tunjukkan value n...
	print(n)

## In this example i will create a multiplication table..

table = 4
lines = 12

# Dari 1 sehingga 13 (tak termasuk 13)
for n in range(1, lines+1):
	# Print / tunjukkan
	# 1,2,3,4,5 -> str(n)-> tukarkan number kepada string
	# + => gabungkan perkataan character
	# 1 x 4 = 4
	# 2 x 4 = 8
	print(str(n) +" x "+str(table)+" = "+ str(n * table));

# Declaring a function (without argument, without return data)
def say_hello():
	print("Hello!")

#Invoking / running a function
say_hello()

#Declaring function with 1 parameter..
def say_goodbye(name):
	print("Goodbye "+name)

say_goodbye("Muzaffar")
say_goodbye("Walid")

#Declaring function with 1 parameter and 1 return data
def hasil_tambah(a,b):
	return a + b

print(hasil_tambah(3,2))
print(hasil_tambah(5,9))



