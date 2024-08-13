#!/usr/bin/python3
""" Rotate """


def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ rotate_2d_matrix """
    rotate_2d_matrix(matx)
    print(matx)