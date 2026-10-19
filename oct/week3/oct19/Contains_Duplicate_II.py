class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen=set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if i>=k:
                seen.remove(nums[i-k])
        return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        