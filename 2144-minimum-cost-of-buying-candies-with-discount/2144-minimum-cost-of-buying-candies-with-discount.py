class Solution(object):
    def minimumCost(self, cost):
        """
        2 2 5 6 7 9

        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<=2:
            return sum(cost)
        else:
            total=0
            cost.sort()
            for i in range(len(cost)-1,-1,-3):
                if i>=0:
                    total+=cost[i]
                if i-1>=0:
                    total+=cost[i-1]
            
            return total


