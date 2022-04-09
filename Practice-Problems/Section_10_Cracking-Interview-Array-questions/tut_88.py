""" Missing Number"""

myList = [1,2,3,4,6,7,8]
size = len(myList)+1

def missing_num(myList, size):
    return int((size*(size+1)/2) - sum(myList))

print(missing_num(myList, size))
