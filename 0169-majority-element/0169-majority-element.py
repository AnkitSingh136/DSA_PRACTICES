class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)
        nums.sort()
        mid=(start+end)//2
        return nums[mid]
        