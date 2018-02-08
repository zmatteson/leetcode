class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        """
        length = len(matrix)-1
        start = 0
        layers = len(matrix)//2
        for j in range(layers):
            for x in range(length):
                swapQ2(matrix, start, length, x)
                swapQ3(matrix, start, length, x)
                swapQ4(matrix, start, length, x)
            layers -= 1
            length -= 2
            start+=1
def swapQ2(matrix, start, length, x):
    end = length
    temp = matrix[start][x+start]
    matrix[start][x+start] = matrix[x+start][start+end]
    matrix[x+start][end+start] = temp
def swapQ3(matrix, start, length, x):
    end = length
    temp = matrix[start][x+start]
    matrix[start][x+start] = matrix[end+start][start+end-x]
    matrix[end+start][start+end-x] = temp
def swapQ4(matrix, start, length, x):
    end = length
    temp = matrix[start][x+start]
    matrix[start][x+start] = matrix[end-x+start][start]
    matrix[end-x+start][start] = temp