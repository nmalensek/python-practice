'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        prevNum = nums[len(nums) - 1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == prevNum:
                del nums[i]
            prevNum = nums[i]

        return len(nums)


run_it = Solution()
print(run_it.removeDuplicates([1,1,2]) == 2)
print(run_it.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5)
print(run_it.removeDuplicates([1,1]) == 1)
print(run_it.removeDuplicates([]) == 0)
print(run_it.removeDuplicates([1]) == 1)

