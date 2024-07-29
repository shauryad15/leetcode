class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start <= end:
            mid = (start + end) // 2
            element = matrix[mid // n][mid % n]
            if element == target:
                return True
            elif element < target:
                start = mid + 1
            else:
                end = mid - 1

        return False