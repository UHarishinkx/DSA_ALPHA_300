class Solution(object):
    def containsDuplicate(self, nums):
        n=set()
        for num in nums:
            if num in n:
                return True
            n.add(num)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        