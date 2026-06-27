class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low=prices[0]
        result=0
        for i in range(1,len(prices)):
            result=max(result,prices[i]-low)
            low=min(low,prices[i])
        return result


        