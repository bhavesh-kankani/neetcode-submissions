class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        idx = high
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