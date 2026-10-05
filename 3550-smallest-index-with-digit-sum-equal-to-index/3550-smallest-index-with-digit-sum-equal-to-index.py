class Solution:
    def smallestIndex(self, num: List[int]) -> int:
        for i in range(len(num)):
            current=num[i]
            sum=0
            while current>0:
                a=current%10
                sum+=a
                current=current//10
            if i==sum:
                return i
        return -1

        