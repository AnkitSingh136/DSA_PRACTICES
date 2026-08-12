class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        maxi=0
        count=0
        h={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]]=1
            else:
                h[nums[i]]+=1
            if h[nums[i]]>k:
                while(h[nums[i]]>k):
                    h[nums[left]]-=1
                    left+=1
            maxi=max(maxi,i-left+1)
        
        return maxi

        