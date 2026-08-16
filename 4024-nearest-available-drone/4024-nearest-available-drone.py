class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        ind=-1
        r1=float('inf')
        for i in range(len(drones)):
            x=drones[i][0]
            y=drones[i][1]
            r=drones[i][2]
            t=abs(x-target[0])+abs(y-target[1])
            if t<=r:
                newr1=min(r1,t)
                if newr1<r1:
                    ind=i
                    r1=newr1
        return ind
        