class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        reservedSeats.sort(key=lambda x: x[0])
        ans=0
        i=0
        while i<len(reservedSeats):
            row=reservedSeats[i][0]
            seats=set()
            while i<len(reservedSeats) and reservedSeats[i][0]==row:
                seats.add(reservedSeats[i][1])
                i+=1
            left=all(s not in seats for s in range(2,6))
            middle=all(s not in seats for s in range(4,8))
            right=all(s not in seats for s in range(6,10))
            if left and right:
                ans+=2
            elif left or middle or right:
                ans+=1
        reserved_rows=len(set(row for row, seat in reservedSeats))
        ans+=(n-reserved_rows)*2

        return ans