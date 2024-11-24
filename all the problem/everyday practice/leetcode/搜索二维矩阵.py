from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left, right = -1, n*m
        while left+1 < right:
            mid = (left+right)//2
            i = mid//m
            j = mid % m
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right = mid
            else:
                left = mid
        return False
