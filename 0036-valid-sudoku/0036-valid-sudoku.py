class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            temp=[j for j in i if j!="."]
            if len(temp)!=len(set(temp)):
                return False
        for i in range(9):
            temp=[board[j][i]  for j in range(9) if board[j][i]!="."]
            if len(temp)!=len(set(temp)):
                return False

        for i in range(3):
            for j in range(3):
                temp=[board[3*i+k][3*j+l] for k in range(3) for l in range(3) if board[3*i+k][3*j+l]!="."]
                if len(temp)!=len(set(temp)):
                    return False
        return True
