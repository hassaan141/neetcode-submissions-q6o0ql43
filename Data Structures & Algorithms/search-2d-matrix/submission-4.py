class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        m = -1
        # figure out which row its in

        top = 0
        bottom = rows

        while top <= bottom:

            mid = top + ((bottom - top) //2)

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                m = mid
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1

        if m == -1:    
            return False
            
        
        # binary search the array

        l = 0
        r = len(matrix[m]) - 1
        while l <= r:

            middle = l + ((r - l) //2)
            if target == matrix[m][middle]:
                return True
            elif target > matrix[m][middle]:
                l = middle + 1
            elif target < matrix[m][middle]:
                r = middle - 1
            
        return False



        
        