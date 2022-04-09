"""Creating an Array"""
from array import *

arr1 = array("i", [1, 2, 3, 4])
print(arr1)

arr2 = array("i", list(map(int, input().split())))
print(arr2)
