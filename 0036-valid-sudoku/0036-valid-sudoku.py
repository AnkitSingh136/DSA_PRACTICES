class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #row cheack 
        
        for i in range(9):
            hr={}
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in  hr:
                        hr[board[i][j]]=1
                    else:
                        return False
        
        #column cheack

        for i in range(9):
            hc={}
            for j in range(9):
                if board[j][i]!='.':
                    if board[j][i] in hc:
                        return False
                    else:
                        hc[board[j][i]]=1
        

        #3*3 block

        for row in range(0,9,3):
            for col in range(0,9,3):
                hb={}
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[j][i]!='.':
                            if board[j][i] in hb:
                                return False
                            else:
                                hb[board[j][i]]=1
        
        return True





        

        




      

        