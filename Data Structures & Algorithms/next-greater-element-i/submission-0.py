class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_hash = {}
        for i in range(len(nums2)):
            nums2_hash[nums2[i]] = i
        
        # next greater array formation in res
        res = [-1]*len(nums2)
        stack = [-1]
        for idx in range(len(nums2)-1, -1, -1):
            while stack[-1] != -1 and nums2[stack[-1]] < nums2[idx]:
                stack.pop()
            if stack[-1] != -1 and nums2[stack[-1]] > nums2[idx]:
                res[idx] = stack[-1]
            stack.append(idx)
        ans = []
        for num in nums1:
            idx = res[nums2_hash[num]]
            ans.append(idx if idx == -1 else nums2[idx])
        return ans