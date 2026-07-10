class Solution(object):
    def isPalindrome(self, s):
        i=0
        j=len(s)-1
        while(i<j):
            left=s[i].lower()
            right=s[j].lower()
            if left.isalnum()  and right.isalnum():
                if left==right:
                    i=i+1
                    j=j-1
                else:
                    return False
            elif left.isalnum():
                j=j-1
            else:
                i=i+1
        return True

        