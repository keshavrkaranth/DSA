'''
Rotate matrix 90 degree
123    741
456 ==>852
789    963
'''
import numpy


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

myArray = numpy.array(matrix)


print(numpy.rot90(myArray,len(myArray)))


def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

print(rotate_matrix(myArray))


