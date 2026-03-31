class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        t = 0
        b = len(matrix) - 1
        row = -1

        while t<=b:

            m = (t + b) // 2

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                row = m
                break
            elif target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1

        if row == -1:
            return False

        arr = matrix[row]
        l = 0
        r = len(arr) - 1

        while l<=r:

            m = (l + r) // 2

            if arr[m] == target:
                return True
            elif target > arr[m]:
                l = m + 1
            elif target < arr[m]:
                r = m - 1
        
        return False

        