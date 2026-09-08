class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        10000020
        :rtype: int
        """
        count=0
        for i in range(1000,n+1):
            s=str(i)
            if len(s)>3:
                count+=1
        return count

        

        