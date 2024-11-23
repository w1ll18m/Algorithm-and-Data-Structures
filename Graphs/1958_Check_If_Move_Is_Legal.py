from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            i, j = rMove + direction[0], cMove + direction[1]

            # check if immediate neighbour (in the line) is opposite colour
            if i not in range(8) or j not in range(8) or board[i][j] == color or board[i][j] == '.':
                continue
            
            # if the immediate neighbour is opposite color then check the next cell
            i, j = i + direction[0], j + direction[1]
            
            # check if there exists another cell in that line of the same colour
            while i in range(8) and j in range(8):
                if board[i][j] == color:
                    return True
                # if the next cell in the line is '.' then the line has ended
                if board[i][j] == '.':
                    break
                # if the cell is the opposite color then move to the next one in the line
                i, j = i + direction[0], j + direction[1]
        
        return False
                
    '''
    board[r][c] = '.' for free cells
    board[r][c] = 'W' for white cells
    board[r][c] = 'B' for black cells
    move -> change it to the colour you are playing as
    good line -> line of three or more cells where endpoints are of one colour and remaining cells are the opposite colour
    legal move -> changed cell becomes the endpoint of a good line

    check if move is legal -> check lines in all 8 directions
        - check if the immediate neighbour is the opposite colour
        - check if there exists another cell in that line of the same colour
    we explore each cell at most once thus total time complexity is O(64)
    ''' 
        