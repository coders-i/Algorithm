#!/usr/bin/env python
# coding: utf-8

# # Between Two Sets

# You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
# 
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
# 
# For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value. Similarly, ,  and , .
# 
# Function Description
# 
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
# 
# getTotalX has the following parameter(s):
# 
# a: an array of integers
# b: an array of integers
# Input Format
# 
# The first line contains two space-separated integers,  and , the number of elements in array  and the number of elements in array .
# The second line contains  distinct space-separated integers describing  where .
# The third line contains  distinct space-separated integers describing  where .
# 
# Constraints
# 
# Output Format
# 
# Print the number of integers that are considered to be between  and .
# 
# Sample Input
# 
# 2 3
# 2 4
# 16 32 96
# Sample Output
# 
# 3
# Explanation
# 
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
# 
# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.

# In[40]:



def getTotalX(a, b):
    # Write your code here
    nmax, nmin, count = max(a), min(b), 0
    
    for i in range(1, (nmin//nmax)+1):
        if (sum((i*nmax) % n for n in a)) + sum((n % (i*nmax) for n in b)) == 0:
            count+=1
    return count
    
    
a=[2,6]
b=[24,36]
print(getTotalX(a,b))

