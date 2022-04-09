"""Linear search in Array"""
from array import *

arr1 = array("i", [1, 2, 3, 4, 5, 6])


def linearSearch(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return "This element is not in the array"


key = int(input())
print(linearSearch(arr1, key))
