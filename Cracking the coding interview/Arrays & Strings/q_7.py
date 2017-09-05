'''
Problem: Rotate Matrix
Description: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Solved: Halve. Don't know how to do it in-place, did see a 1-line solution on the internet: zip(*matrix[::-1])
'''

def rotate_clockwise(m):
    rotated = []
    for i in range(len(m)):
        row = []
        for j in range(len(m)-1, -1, -1):
            row.append(m[j][i])
        rotated.append(row)

    return rotated

def rotate_counterclockwise(m):
    rotated = []
    
    for j in range(len(m)-1, -1, -1):
        row = []
        for i in range(len(m)):
            row.append(m[i][j])
        rotated.append(row)

    return rotated

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate_clockwise(matrix))
print(rotate_counterclockwise(matrix))