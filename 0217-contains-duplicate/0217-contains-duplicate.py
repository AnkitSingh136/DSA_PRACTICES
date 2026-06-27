class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h={}
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            else:
                h[nums[i]]=1
        return False

        