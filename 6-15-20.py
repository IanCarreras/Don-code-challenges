# -*- coding: utf-8 -*-
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array)
# some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Input:
# [4,3,2,7,8,2,3,1]

# Output: 
# [2,3]

# first solution
def twice(array):
    new_array = []
    placeholder = []
    for n in array:
        if n in placeholder:
            new_array.append(n)
        placeholder.append(n)
    return new_array


output = twice([4,3,2,7,8,2,3,1])
print(output)