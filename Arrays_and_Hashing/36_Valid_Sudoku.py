class Solution(object):
    def isValidSudoku(self, board):                                 # O(1) solution
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [{} for i in range(9)]                               # O(1) because constant loop
        columns = [{} for i in range(9)]
        boxes = [[{} for i in range(3)] for i in range(3)]

        for i in range(9):                                          # let i represent the current row
            for j in range(9):                                      # let j represent the current column
                if board[i][j] == ".":                              # "." do violate any of the rules
                    continue
                
                if board[i][j] in rows[i]:                          # check if number already exists in row
                    return False
                else:
                    rows[i][board[i][j]] = True
                
                if board[i][j] in columns[j]:                       # check if number already exists in column
                    return False
                else:
                    columns[j][board[i][j]] = True
                
                i2 = int(i / 3)
                j2 = int(j / 3)
                if board[i][j] in boxes[i2][j2]:                    # check if number already exists in box
                    print(boxes[i2][j2])
                    print(board[i][j])
                    return False
                else:
                    boxes[i2][j2][board[i][j]] = True
        
        return True
                
        # keep track of numbers used in columns, rows, boxes
        # given boxes[i][j], we say that boxes[0][0] represents the upper left box
        #                                boxes[0][1] represents the upper middle box
        #                                boxes[1][0] represents the middle left box
        # pattern: check if number exists -> use a hash map for each column/row/box for O(1) verify

        
        