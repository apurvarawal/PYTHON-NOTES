# USED FOR COMMENT

my_message = 'Hello World'
my_message2 = 'harry\'s world' # we can use this '\', to escape the single quote, to help the compiler to understand that, its aphostrophe
my_message3 = "harry's world"  # or we can use double quotes instead
my_message4 = """harry's world was
a very happy world"""          # we can use single or double quotes triple times on both sides to print multi line output
print(my_message)
print(my_message2)
print(my_message3)
print(my_message4)

print(len(my_message))         # 'len' is used to print the length of the string
print(my_message[6])           # by this way, we can print the alphabet or number on the particular index, starting from 0 to (len-1)
print(my_message[0:4])         # it will print alphabets from index 0 to 4, including index 0 and excluding index 4
print(my_message[:4])          # it will automatically start index from 0
print(my_message[5:])          # it will automatically end index till last
print(my_message.upper())      # used to convert all alphabets to upper case
print(my_message.lower())      # used to convert all alphabets to lower case
print(my_message.count('l'))   # tells the number of that particular alphabet or word
print(my_message4.find('was')) # tells the number of index, at which the alphabet is present or the starting index of that word
print(my_message.find('universe'))  # returns '-1', when it can't find that word or alphabet

new_my_message = my_message.replace('World', 'universe') # or we can simply write my_message , instead of new_my_message, if we want to update it
print(new_my_message)

# CONCATENATION
greeting = 'Hello'
name = 'Aditya'
message = greeting + ', ' + name
print(message)

# FORMATTING
formatted_message = '{}, {}. Welcome!'.format(greeting, name) # here, the first bracket will get the first variable value in format, and second will second, and so on
print(formatted_message)

# F string
f_string_message = f'{greeting}, {name.upper()}. Welcome!'
print(f_string_message)

print(dir(name)) # prints all the attributes, that can be applied on the variable
print(help(str)) # prints all the attributes with explanation that can be applied on the variable
print(help(str.lower)) # prints the explanation of that specific attribute