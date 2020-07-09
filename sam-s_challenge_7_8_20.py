# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175

# sort each sub array
# add all the elements from the first position of each sub array

array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def sum_of_minimum(arr):
    sum = 0
    for i in arr:
        i.sort()
        sum += i[0]
    return sum

result = sum_of_minimum(array)
print(result)