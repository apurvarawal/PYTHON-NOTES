def hello_func():
    pass              # used for empty functions

print(hello_func)     # does not execute the function

print(hello_func())   # prints the returned value of the function

def hi_func():
    print('hi function!')

hi_func()             # executes the function

def jk():
    return 'just kidding'

print(jk())

print(jk().upper())    # prints the returned string in upper case
print(len(jk()))       # prints the length of the returned string

#### --- Passing PARAMETERS to functions --- ####

def hello_function(greeting):
    return '{} function!' .format(greeting)

print(hello_function('namaste!'))

# Putting default value to a parameter

def hi_function(greeting, name = 'you'):
    return '{} {}' .format(greeting, name)

print(hi_function('namaste'))

print(hi_function('namaste', 'apurva'))

#### --- ARGS and KWARGS --- ####

def student_info(*args, **kwargs):     # used for arbitrary values
    print(args)
    print(kwargs)

courses = ['maths', 'english']
info = {'name': 'apurva', 'age': 20}

student_info(*courses, **info)         # '*' , '**' are used to unpack values of courses and info