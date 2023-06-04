### --- FOR LOOP --- ###
nums = [1,3,4,5,6,9]

for num in nums:
    print(num)

### --- Break and Continue --- ###

for num in nums:
    if num == 5:
        print('found it')
        break                # stop printing elements when 5 will be found
    print(num)

for num in nums:
    if num == 5:
        print('found it')
        continue             # it will continue to print elements
    print(num)

# Loop in loop

for num in nums:
    for letter in 'abc':
        print(num, letter)
    
# Range

for i in range(1, 11):
    print(i)


### --- WHILE LOOP --- ###

x = 0
while x < 10:
    print(x)
    x += 1