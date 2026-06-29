import random
class Solution:
    def partition(self, low, high, pivot_index):
        self.array[low], self.array[pivot_index] = self.array[pivot_index], self.array[low]
        i = low + 1
        j = i
        while j <= high:
            if self.array[j] < self.array[low]:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1
            j += 1
        self.array[low], self.array[i-1] = self.array[i-1], self.array[low]
        return i-1

    def quicksort(self, low, high):
        if low >= high:
            return
        
        pivot_index = random.randint(low, high)
        p_index = self.partition(low, high, pivot_index)
        self.quicksort(low, p_index-1)
        self.quicksort(p_index+1, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.array = nums
        self.quicksort(0, len(self.array)-1)
        return self.array