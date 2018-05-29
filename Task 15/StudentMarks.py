'''
Created on Mon May 28 13:40:25 2018

@author: hamza

Sorting student marks according to ages using numpy
'''
# import numpy
from numpy import * 

# generate 1D arrays with randomly generated ages/marks of size 200
age = random.random_integers(18,40, size=(200))
marks = random.random_integers(0,100, size=(200))

# sort the arrays
sorted_age = sort(vstack((age, marks)), axis=1)
sorted_marks = sort(vstack((age, marks)), axis=1)

print sorted_age   
print sorted_marks