'''
Problem: Zero Matrix
Description: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.
Solved: True
'''

def parse_matrix(m):
    indexes = []

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                indexes.append([i, j])

    for ind in indexes:
        row = ind[0]
        column = ind[1]

        m[row] = [0]*len(m[0])
        for i in range(len(m)):
            m[i][column] = 0

    return m


matrix1 = [[0,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,0,6],[7,8,9]]
matrix3 = [[1,2,3],[4,5,6],[7,8,0]]

print(parse_matrix(matrix1))
print(parse_matrix(matrix2))
print(parse_matrix(matrix3))