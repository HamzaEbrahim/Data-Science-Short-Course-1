"""
Created on Wed May 30 10:20:28 2018

@author: hamza

task demonstrating simple mathematical operations using arrays
"""
# import numpy
from numpy import *

# create array called my_arr1 in form (2,4)
a = [[0,1,2,3],[10,11,12,13]]
my_arr1 = array(a)

# create a second array in formm(1,4) called my_arr2
b = [[2,-1,1,0]]
my_arr2 = array(b)

# multiply my_arr1 and my_arr2, then print the result
product = multiply(my_arr1, my_arr2)
print product

# create variable arr_one by multiplying my_arr2 by 200
arr_one = multiply(my_arr2, 200)

# create variable arr_two by multiplying my_arr2 by 200.0
arr_two = multiply(my_arr2, 200.0)

# print the arrays arr_one and arr_two
print arr_one
print arr_two

# typecode of arr_one and arr_two are slightly different. elements in arr_one are integers while elements in arr_two are floats.
print arr_one == arr_two