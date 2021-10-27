# Import and Use numpy
import numpy as np

# Create a matrices (1 x 3)

arr = np.array([1,3,4])

# print(arr)
# print(arr.shape)
# Create a matrices (2 x 3)

arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr)

# Create a matrices ( 3 x 3 x 3)

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(arr.shape)
#print(arr)

a = np.array([[3,-7],[5,2],[1,1]])
#print(a)
#Remember that just like array, it start with index 0..
# If you try to get the value 2  a22, you have to minus 1
#print(a[1,1])
#print(a[2,0])
#print(a[2,1])

# the first index is the row, second index is the column
b = np.array([[1,-2,5],[-3,2,9]])
#the first row / print the first row
#print(b[0,:])
# the second row / print the second row
#print(b[1,:])

# All the element in the first , second and thirdcolumn
#print(b[:,0])
#print(b[:,1])
#print(b[:,2])

# a = np.array([[6],[-2]])
# b = np.array([[-5],[1]])
# tambah = a + b
# print(tambah)

# a = np.array([[1,-2,4]])
# b = np.array([[2,1,3]])
# minus1 = a - b
# print(minus1)

# a = np.array([[8,-1],[-5,1]])
# b = np.array([[1,3],[3,-4]])
# plus1 = a+b
# print(plus1)

# a = np.array([[3],[1]])
# b = np.array([[-4],[4]])
# c = np.array([[2],[-2]])
# mixop = a+b-c
# print(mixop)
## Scalar multiplication

# c = np.array([[2,-1],[-5,7]])
# print(c)
# c_multi = 3 * c 
# print(c_multi)
# c_multi2 = 1/6 * c
# print(c_multi2)

#vector multiplication
# a1 = np.array([[1,2]])
# a2 = np.array([[3],[4]])
# #print(a1)
# #print(a2)
# va1_a2 = a1.dot(a2)
# print(va1_a2)

# b1 = np.array([[-2,0],[3,5]])
# b2 = np.array([[1],[0]])
# vb1_b2 = b1.dot(b2)
# print(vb1_b2)

# c1 = np.array([[-3,0],[2,1]])
# oper = c1.dot(c1) + 4 * c1
# print(oper)


# b = np.array([[-1,3,7],[2,4,1],[3,5,2]])
# bt = b.T
# print(bt)

# a = np.array([[2,4],[-2,-3]])
# b = np.array([[1,1],[3,6]])
# deta = np.linalg.det(a)
# detb = np.linalg.det(b)
# print(deta)
# print(detb)

# productab  = a.dot(b)
# print(productab)

# detproductab = np.linalg.det(productab)
# print(detproductab)
# productdet = deta * detb
# print(productdet)

#This is the function, it will take 3 parameters
# 1st parameter is the matrix
# 2nd parameter is the row
# 3rd parameter is the column


# The function delete will remove the specific column or
# row defined in the second parameter
# the third parameter will define either it will determine eiter the row or column
# 0 - row, 1 means colum
def minorOfAMatrix(A,i,j):
	rowOperation = np.delete(A,i,0)
	columnOperation = np.delete(rowOperation,j,1)
	return columnOperation


# matrix = np.array([[1,1,1],[0,1,1],[0,0,1]])
# minor1 = minorOfAMatrix(matrix,0,0)
# # print(minor1)
# detminor1 = np.linalg.det(minor1)
# # print(detminor1)

# minor2 = minorOfAMatrix(matrix,0,1)
# detminor2 = np.linalg.det(minor2)
# # print(minor2)
# # print(detminor2)
# minor3 = minorOfAMatrix(matrix,0,2)
# detminor3 = np.linalg.det(minor3)
# print(minor3)
# print(detminor3)

# Recap

a = np.eye(1)
b = np.eye(2)
c = np.eye(3)
print(a)
print(b)
print(c)

# np.random.seed(123)

# a = np.random.randint(0,10, size=(3,3))
# b = np.random.randint(0,10, size=(3,3))
# print(a)
# print(b)

# a = np.array([[3,1],[0,-1]])
# rev_a = np.linalg.inv(a)
# # print(rev_a)

# b = np.array([[-2,-1],[0,3]])
# rev_b = np.linalg.inv(b)
# print(rev_b)

# A = np.array([[1,2,1],[1,3,0],[0,-1,8]])
# B = np.array([[1],[2],[3]])
# print(A)
# X = A-1 * B
# X = np.linalg.inv(A).dot(B)
# print(X)

A = np.array([[4,3,2],[-2,2,3],[3,-5,2]])
B = np.array([[25],[-10],[-4]])
X = np.linalg.inv(A).dot(B)
X2 = np.linalg.solve(A,B)
print(X)
print(X2)

