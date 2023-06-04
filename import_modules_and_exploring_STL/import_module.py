print('imported module')

test = 'test string'

def find_idx(to_search, target):

    for i, value in enumerate(to_search):
        if value == target:
            return 1
        
    return -1
