#!/usr/bin/env python
# coding: utf-8

# # Staircase
# 

# Consider a staircase of size :
# 
#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# 
# Write a program that prints a staircase of size .
# 
# Function Description
# 
# Complete the staircase function in the editor below. It should print a staircase as described above.
# 
# staircase has the following parameter(s):
# 
# n: an integer
# Input Format
# 
# A single integer, , denoting the size of the staircase.
# 
# Constraints
# 
#  .
# 
# Output Format
# 
# Print a staircase of size  using # symbols and spaces.
# 
# Note: The last line must have  spaces in it.
# 
# Sample Input
# 
# 6 
# Sample Output
# 
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# Explanation
# 
# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .

# In[7]:


def staircase(n):
    i=0
    while i<n:
        for j in range(0,n-i-1):
            print(' ',end='')
        for k in range(0,i+1):
            print('#',end='')
        print()
        i+=1

staircase(6)
