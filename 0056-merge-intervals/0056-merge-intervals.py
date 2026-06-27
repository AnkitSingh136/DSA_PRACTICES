class Solution(object):
    def merge(self, intervals):
        """
        result=[]
        start=1
        end=3

        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if end<intervals[i][0]:
                result.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            elif end>=intervals[i][0]:
                if start>intervals[i][0]:
                    start=intervals[i][0]
                if end<=intervals[i][1]:
                    end=intervals[i][1]
        result.append([start,end])
        return result



            

        