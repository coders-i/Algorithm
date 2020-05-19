#!/usr/bin/env python
# coding: utf-8

# # Time Conversion

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# 
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
# 
# Function Description
# 
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# 
# timeConversion has the following parameter(s):
# 
# s: a string representing time in  hour format
# Input Format
# 
# A single string  containing a time in -hour clock format (i.e.:  or ), where  and .
# 
# Constraints
# 
# All input times are valid
# Output Format
# 
# Convert and print the given time in -hour format, where .
# 
# Sample Input 0
# 
# 07:05:45PM
# Sample Output 0
# 
# 19:05:45

# In[26]:


def timeConversion(s):
    
    hr,mi,sec=s.split(':')
    sec,me=sec[0:2],sec[-2:]
    
    if me=='PM':
        if 0<int(hr)<=11:
            hr=str(int(hr)+12)
    
    if me=='AM':
        if int(hr)==12:
            hr=str('00')
            
    return hr+':'+mi+':'+sec

if __name__ == '__main__':

    s = '11:59:59PM'

    result = timeConversion(s)

    print(result , '\n')

