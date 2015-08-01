# find the laregest sum submatrix in a matrix

import pdb
def largest_array(array):
    size = len(array)
    start = [0 for i in range(size)]
    end = [0 for i in range(size)]
    z = [0 for i in range(size)]
    z[0] = array[0]
    for i in range(1,size):
        if z[i-1]+array[i] > array[i]:
            z[i] = z[i-1]+array[i]
            end[i] = end[i-1] + 1
            start[i] = start[i-1]
        else:
            z[i] = array[i]
            start[i] = i
            end[i] = i

    max_index = 0
    max_value = z[0]
    for i in range(1,size):
        if z[i] > max_value:
            max_index = i
            max_value = z[i]
    return (start[max_index],end[max_index],max_value)



def largestSum(matrix):
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0
    max_value = 0
    cols = len(matrix[0])
    tmp = matrix[0]
    rows = len(matrix)
    for i in range(rows):
        for j in range(i,rows):
            for k in range(cols):
                tmp[k] += matrix[j][k]
            first,second,value = largest_array(tmp)
            if value > max_value:
                max_left = first
                max_right = second
                max_up = i
                max_down = j
                max_value = value

    return max_value



