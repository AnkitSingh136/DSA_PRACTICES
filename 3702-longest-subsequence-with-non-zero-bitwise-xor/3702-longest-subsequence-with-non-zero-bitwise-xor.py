class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        result=0
        c=0
        zero=0
        for i in range(len(nums)):
            if result^nums[i]!=0:
                result^=nums[i]
                c+=1
            else:
                zero+=1
                result=0
        if c==0:
            return 0
        return c+zero-1 if result==0 else c+zero
            
            




        