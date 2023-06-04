student = {'name' : 'Apurva', 'age' : 20, 'courses' : ['math', 'compsc']}

print(student)
print(student['name'])  # this will throw an error if we write key that dont exist
print(student.get('phone'))  # to avoid above mentioned error, we use get method, it returns none for inexisting key
print(student.get('phone', 'NOT FOUND'))  # we can put a default value for keys that are not found

# Add or Update SINGLE keys
student['phone'] = '333-333'  # this is how we add new key or update existing key in the dictionary
print(student.get('phone', 'NOT FOUND'))  

# Add or Update MULTIPLE keys
 
student.update({'name': 'Aditya', 'age' : 21, 'fav_sub' : 'physics'}) # this is used when we want to update or add multiple keys
print(student)

# Delete key

del student['age']
print(student)

# Pop key

popped_key = student.pop('fav_sub')
print(popped_key)

print(student)

print(len(student))  # prints the number of key value pairs
print(student.keys())   # prints all the keys of student dictionary
print(student.values())  # prints values of all keys
print(student.items())   # prints all key value pairs

# Loop in dictionary

for key, value in student.items():
    print(key, value)