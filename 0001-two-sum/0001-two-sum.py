class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        for i in range(len(nums)):
            if target-nums[i]  in h:
                return [i,h[target-nums[i]]]
            if nums[i] not in h :
                h[nums[i]]=i
        
