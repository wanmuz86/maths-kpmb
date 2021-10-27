# to use sqrt function, need to import math library
import math

# x^2 + 3x + 1 = 0
# create function to find the   values of x
# -b +- sqrt(b^2 - 4ac) / 2a

a = 1
b = 3
c = 1

middle = math.sqrt(b**2 - 4*a*c)

ans1 = -b + middle / 2*a
ans2 = -b - middle / 2*a

print(ans1)
print(ans2)

