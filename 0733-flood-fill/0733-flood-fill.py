class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        value=image[sr][sc]
        if value==color: 
            return image
        def change(i,j,value,m,n):
            if i<0 or j<0 or i>=m or j>=n or image[i][j]!=value:
                return
            image[i][j]=color
            change(i+1,j,value,m,n)
            change(i-1,j,value,m,n)
            change(i,j+1,value,m,n)
            change(i,j-1,value,m,n)
        change(sr,sc,image[sr][sc],len(image),len(image[0]))
        return image
        