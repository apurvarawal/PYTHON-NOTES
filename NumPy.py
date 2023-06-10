###### --- IMP LINKS --- ######
🔗 Indexing: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.indexing.html
🔗 Array Creation Routines: https://numpy.org/doc/stable/reference/routines.array-creation.html
🔗 Math Routines Docs: https://numpy.org/doc/stable/reference/routines.math.html
🔗 Linear Algebra Docs: https://numpy.org/doc/stable/reference/routines.linalg.html


# -> it is faster than lists because it uses fixed datatype, i.e., it sees data in binary
# -> NumPy uses contiguous memory

import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[1,2,3], [4,5,6]])
print(b)

# for finding the dimension of an array

print(a.ndim)
print(b.ndim)

# for finding the (m x n) of a matrix

print(a.shape)
print(b.shape)

# for finding the datatype

print(a.dtype)
print(b.dtype)

# we can also specify the data type we want to store

c = np.array([1,4,5], dtype='int16')
print(c.dtype)

# for finding datatype size(bytes)

print(a.itemsize)
print(c.itemsize)

# for getting a SPECIFIC element

d = np.array([[1,2,3,4,5,6,7,8], [4,5,6,7,8,9,0,1]])
print(d[1, 6])            # --- it means d[row, column]

# for getting a SPECIFIC ROW

print(d[0, :])            # indexing starts from '0'

# for getting a SPECIFIC COLUMN

print(d[: , 1])

# to print specific elements of a row and eliminate others

print(d[0, 1:7:2])         # d[row, column starting index: column ending index: index gap]

# Updating a specific location

d[0,3] = 7
print(d)

e = np.array([[[1,6],[5,8]], [[7,2], [3,8]]])
print(e)
print(e[0,1,1])             # it means print (1,1) element of 0th array
e[:, 1, :] = 0              # it means update all the elements of row 1 in each array 
print(e)
e[1, 1, :] = 3
print(e)                    # it means update all the elements of row 1 in 1st array 

# All ZERO array

f = np.zeros((2,2))         # (2,2) is the (row, col) of the matrix
print(f)

# All ONES array

g = np.ones((2,3))
print(g)

# All same number array

h = np.full((2,4), 3)       # (2,4) is the (row, col) of the matrix and 3 is the number that has to be filled in the matrix
print(h)

# making an array like the size of the previous any array and filling it with a number of our choice

i = np.full_like(a, 8)
print(i)

j = np.full(a.shape, 8)
print(j)

#### we can use any of the above mentioned way for this

# RANDOM DECIMAL array

k = np.random.rand(4,5)
print(k)

# RANDOM INTEGER array

l = np.random.randint(6, size=(6,7))      # 6 is the end value for random integers
print(l)

m = np.random.randint(2,6, size=(6,7))      # 2 is the starting value and 6 is the end value for random integers
print(m)

# IDENTITY MATRIX

n = np.identity(3)             # 3 is the size of the array
print(n)

# REPEAT an array

o = np.array([[1,2,3]])
rpt = np.repeat(o, 4, axis=0)     # here (o,4,axis=0) means (array to be repeated, number of times it to be repeated, axis)
print(rpt)


#### --- QUES : make array 
""" 1 1 1 1 1
    1 0 0 0 1
    1 0 9 0 1
    1 0 0 0 1
    1 1 1 1 1 """

a1 = np.ones((5,5))
print(a1)

a2 = np.zeros((3,3))
print(a2)

a2[1,1] = 9
print(a2)

a1[1:4,1:4] = a2               # a1[row start: row end, col start: col end] = a2
print(a1)

##### BEWARE while copying 

b1 = np.array([1,2,3])
b2 = b1 
b2[0] = 100
print(b1)           # this will show changes in b1 also, that we made for b2, because we are not copying b1 in b2, by using '=' sign
                    # we are meaning that both b1 and b2 point to the same array
print(b2)

# to solve the above problem, we use copy() function

c1 = np.array([4,5,6])
c2 = c1.copy()
c2[0] = 8
print(c1)
print(c2)

#### --- to add, subtract , multiply or divide in each element of the array, we simply write
b1 += 3
print(b1)

b1 -= 1
print(b1)

b1 *= 2
print(b1)

b1 = b1 / 2
print(b1)

# for POWER
b1 = b1 ** 2
print(b1)

# for SINE
b1 = np.sin(b1)
print(b1)


## multiplying matrices of different shapes

d1 = np.full((2,3), 3)
print(d1)

d2 = np.full((3,2), 2)
print(d2)

d3 = np.matmul(d1,d2)    # this will multiply the matrices, just like we do in maths
