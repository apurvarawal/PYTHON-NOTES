### COMPARISONS ###
# Equal                           ==
# Not equal                       !=
# Greater than                    >
# Less than                       <
# Greater than or equal to        >=
# Less than or equal to           <=
# Object Identity                 is     {checks if 2 objects have same identity or not}


### --- CONDITIONALS --- ###

language = 'C++'

if language == 'PYTHON':
    print('language is python')
elif language == 'C++':
    print('language is C++')
else:
    print('condition is false')


### BOOLEANS ###
# and
# or
# not


## and ##
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

## or ##
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')

## not ##
user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('Welcome')


##### --- Difference between '==' and 'is' --- #####

a = [1,2,3]
b = [1,2,3]

c = a

print(a==b)
print(a is b)  # prints false, because 'a' and 'b' have different identities
print(c is a)  # prints true, because 'c' and 'a' have same identities

print(id(a))   # this prints the unique id of the object
print(id(b))
print(id(c))


###### ---- False Values ---- ######

# False
# None
# Zero of any numeric type
# Any empty sequence, for example '', (), []
# Any empty map, for example {}

condition = False
if condition:
    print('condition is true')
else:
    print('condition is false')

condition = None
if condition:
    print('condition is true')
else:
    print('condition is false')
    
condition = 0
if condition:
    print('condition is true')
else:
    print('condition is false')