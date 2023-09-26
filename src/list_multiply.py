row = [""] * 3

board = [row] * 3

assert board[0] == ["", "", ""]
assert board[0][0] == ""
assert board == [["", "", ""], ["", "", ""], ["", "", ""]]

board[0][0] = "X"

assert id(row) == id(board[0]) == id(board[1]) == id(board[2])

assert board == [["X", "", ""], ["X", "", ""], ["X", "", ""]]

row[0] = "O"

assert board == [["O", "", ""], ["O", "", ""], ["O", "", ""]]

board = [[""] * 3 for _ in range(3)]
board[0][0] = "X"

assert board == [["X", "", ""], ["", "", ""], ["", "", ""]]
