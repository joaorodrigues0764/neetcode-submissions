class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_ofc = 0
        right_ofc = len(matrix) - 1

        while left_ofc <= right_ofc:
            middle_ofc = (left_ofc + right_ofc) // 2
            
            left = 0
            right = len(matrix[middle_ofc]) - 1
            while left <= right:
                middle = (left + right) // 2

                if matrix[middle_ofc][middle] == target:
                    return True
                
                elif matrix[middle_ofc][middle] < target:
                    left = middle + 1
                
                else:
                    right = middle - 1

            if matrix[middle_ofc][0] < target:
                left_ofc = middle_ofc + 1

            elif matrix[middle_ofc][0] > target:
                right_ofc = middle_ofc - 1

        return False