class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

# Analysis of solution :
"""
Time Complexity :
firstly, there are two loops that iterate over entire matrix O(m*n) m = no. of rows, n = no. of columns
same goes for second loop also, Overall time complexity is O(m*n)

Space Complexity :
At worst case, two sets rows and cols can store m, n values respectively ( NO DUPLICATES), so Space Complexity is O(m+n) 
"""
