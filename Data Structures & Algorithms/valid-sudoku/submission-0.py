class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_dict = {}
            for number in row:
                if number != ".":
                    if number in row_dict:
                        row_dict[number] += 1
                        return False
                    else:
                        row_dict[number] = 1   
        i = 0
        j = 0
        while j < 9:
            column_dict = {}
            while i < 9:
                if board[i][j] != ".":
                    if board[i][j] in column_dict:
                        column_dict[board[i][j]] += 1
                        return False
                    else:
                        column_dict[board[i][j]] = 1
                i += 1
            i = 0
            j += 1
        boxes = [{} for _ in range(9)]
        i = 0
        j = 0
        while j < 9:
            while i < 9:
                if board[i][j] != ".":
                    num = board[i][j]
                    box_index = (i // 3) * 3 + (j // 3)
                    if num in boxes[box_index]:
                        boxes[box_index][num] += 1
                        return False
                    else:
                        boxes[box_index][num] = 1
                i += 1
            i = 0
            j += 1
        return True
