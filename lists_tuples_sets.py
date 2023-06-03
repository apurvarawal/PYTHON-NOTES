# LISTS

subjects = ['Hindi', 'English', 'Maths']

print(subjects)               # prints all the elements present in the list
print(len(subjects))          # prints the number of elements present in the list
print(subjects[1])            # prints element at the given index
print(subjects[-1])           # '-1' always prints last element

print(subjects[0:2])          # prints elements starting from index 0 to 2, including index 0 and excluding index 2

subjects.append('Art')        # adds element to the list in the end
print(subjects)

subjects.insert(0, 'EVS')     # insert element at the given specific location in the list
print(subjects)

subjects_2 = ['Machine Design', 'Thermal Engg']
subjects.insert(0, subjects_2)           # this will insert the whole subjects_2 list in list 1 at index 0, and now the whole subject_2 list will be considered as a single element of subjects list at index 0
print(subjects)
print(subjects[0])

subjects_3 = ['Material sc', 'Biology' , 'History']
subjects.extend(subjects_3)               # this will insert the elements of subjects_3 list in subjects list as separate elements
print(subjects)

# Append and insert work in the same manner, if we want to append a list in another list

subjects.remove('English')               # this removes the mentioned specific element from the list
print(subjects)

popped = subjects.pop()                           # this removes the last element from the list
print(popped)
print(subjects)

subjects.reverse()
print(subjects)

subjects_3.sort()       # sorts in alphabetical or ascending order
print(subjects_3)

subjects_3.sort(reverse=True)     # sorts in reverse order
print(subjects_3)

# sorted(subjects_3)   \\ does not return the sorted list, it just sorts the list, to get the sorted list, we have to equate it to another variable

sorted_list = sorted(subjects_3)
print(sorted_list)

# Min and Max

nums = [ 1, 3, 5, 54]
print(min(nums))         # prints min value of the list
print(max(nums))         # prints max value of the list
print(sum(nums))         # prints sum of values of the list

# FINDING VALUES

print(nums.index(3))     # prints the index of the given element
print(56 in nums)        # tells whether the given element is present in the list or not, through boolean values

for subject in subjects:     # loops through all values of subjects list
    print(subject)

for index , subject in enumerate(subjects):    # loops through all values of subjects list and also gives the index of each element
    print(index, subject)

for index , subject in enumerate(subjects, start=1):    # loops through all values of subjects list and also gives the index of each element, and starts serial number from the given number
    print(index, subject)

# CONVERTING LIST TO STRING

cars = ['WagonR', 'Maruti', 'Audi', 'Mercedes', 'Renault']

cars_str = ', '.join(cars)

print(cars_str)

# CONVERTING STRING TO LIST BY SPLITTING

new_list = cars_str.split(', ')   # we are splitting wherever we find ', ', if we used in ' - ' , in cars_str, then we have to split at ' - '

print(new_list)