import import_module as im                  # we can also import a particular function, but then we can not access any other function from that file
# from import_module import find_idx, test -------(1)      # importing a particular fucntion


courses = ['hindi', 'english', 'maths']

index = im.find_idx(courses, 'english')
# index = find_idx(courses, 'english')    # if we are importing by (1)

print(index)