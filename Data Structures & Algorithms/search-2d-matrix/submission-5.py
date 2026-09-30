class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                break
        if not (low <= high):
            return False
        
        idx = mid
        low, high = 0, len(matrix[mid])-1
        while low <= high:
            mid = (low + high)//2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False