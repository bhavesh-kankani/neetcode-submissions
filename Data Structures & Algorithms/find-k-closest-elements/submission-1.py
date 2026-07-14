class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = r = i = 0
        while i < len(arr)-1 and arr[i] < x:
            i += 1
        
        if i > 0:
            l = r = i if ((arr[i]-x) < (x-arr[i-1])) else i-1
        k -= 1
        while k and r < len(arr)-1 and l > 0:
            if (x-arr[l-1]) <= (arr[r+1]-x):
                print("nce")
                l -= 1
            else:
                r += 1
            k -= 1
        while k and r < len(arr)-1:
            k -= 1
            r += 1
        while k and l > 0:
            k -= 1
            l -= 1
        return arr[l:r+1]