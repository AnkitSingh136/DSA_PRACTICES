class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        add    not add      max
        -1         1         1
        1+-3        -3       1
        -2          4        4
        3           -1       4
        3+2         2        5
        5+1          1        6
        6-5          -5       6
        1+4          4         6
        
        """
        m=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            m=max(m+nums[i],nums[i])
            max_sum=max(max_sum,m)
        return max_sum




        