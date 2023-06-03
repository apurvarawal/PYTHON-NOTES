num1 = 2
num2 = 2.14
print(type(num1)) # prints the type of number
print(type(num2))

print(2+3)  # Addition
print(3-2)  # Subtraction
print(3*2)  # Multiplication
print(3/2)  # Division
print(3//2) # Floor Division , it returns the smallest integer number after division
print(3**2) # Exponent
print(3%2)  # Modulus , returns remainder

# Pyhton follows BODMAS rule of mathematics

num3 = 3
num3 += 1   # we can also use '-=', '*=', '/=' accordingly
print(num3)

print(abs(-3))

print(round(6.79)) # prints nearest integer value
print(round(6.34))
print(round(6.794456, 2)) # prints rounded value till the mentioned decimal places, here its 2

# COMPARISONS
# it returns boolean values

print(3==2)  # equals
print(3!=2)  # not equals
print(3>2)   # greater than
print(3<2)   # less than
print(3>=2)  # greater than or equal to
print(3<=2)  # less than or equal to

num_1 = '100'  #THIS IS A STRING, AND NOT A NUMBER
num_2 = '300'

print(num_1 + num_2) # since num_1 and num_2 are strings, it will lead to concatenation

# CASTING STRINGS TO INTEGERS

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)