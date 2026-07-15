class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = r = i = 0
        while i < len(arr)-1 and arr[i] < x:
            i += 1
        
        if i > 0:
            l = r = i if ((arr[i]-x) < (x-arr[i-1])) else i-1
        k -= 1
        while k:
            if l <= 0:
                r += 1
            elif r >= len(arr)-1:
                l -= 1
            elif (x-arr[l-1]) <= (arr[r+1]-x):
                l -= 1
            else:
                r += 1
            k -= 1
        
        return arr[l:r+1]