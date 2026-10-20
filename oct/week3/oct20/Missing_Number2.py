class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res=0
        exp=0
        for i in range(len(nums)+1):
            if i<len(nums):
                res^=nums[i]
            exp^=i
        return res^exp