class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        def get_highest():
            low, high = 0, n-1
            while low <= high:
                mid = (low + high) >> 1
                if low == high: return low
                if mid-1 < 0: return mid if mountainArr.get(mid) >= mountainArr.get(mid+1) else mid+1

                mid_el = mountainArr.get(mid)
                left_el = mountainArr.get(mid-1)
                right_el = mountainArr.get(mid+1)
                if mid_el > left_el and mid_el > right_el:
                    return mid
                elif mid_el > left_el and mid_el < right_el:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        highest = get_highest()

        # first check in first half
        low, high = 0, highest
        while low <= high:
            mid = (low + high) >> 1
            mid_el = mountainArr.get(mid)
            if mid_el == target: return mid
            elif mid_el < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # second check in second half
        low, high = highest+1, n-1
        while low <= high:
            mid = (low + high) >> 1
            mid_el = mountainArr.get(mid)
            if mid_el == target: return mid
            elif mid_el < target:
                high = mid - 1
            else:
                low = mid + 1
        return -1