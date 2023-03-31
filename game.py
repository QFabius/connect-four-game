nrows = 6
ncols = 7
pieces = ['X', 'O']

def create_board():
  board = []
  for row in range(nrows):
    board_row = []
    for col in range(ncols):
      board_row.append(' ')
    board.append(board_row)
  # print_board(board)
  return board

def print_board(board):
  idx_str = ' '
  row_str = '+'
  for col in range(len(board[0])):
    idx_str += '{INDEX} '.format(INDEX=col+1)
    row_str += '-+'
  print(idx_str)
  print(row_str)

  for row in range(len(board)):
    row_str = '|'
    bound_str = '+'
    for col in range(len(board[row])):
      row_str += '{VALUE}|'.format(VALUE=board[row][col])
      bound_str += '-+'
    print(row_str)
    print(bound_str)

def drop(board, col, piece):
  if col < 1 or col > ncols:
    print("Enter valid column.")
    return board
  if piece not in pieces:
    print("Enter valid piece: X or O.")
    return board
  col -= 1
  for row in range(len(board)-1,-1,-1):
    if board[row][col] == ' ':
      board[row][col] = piece
      break
    elif row == 0:
      print("Column full. Choose other column.")
  # print_board(board)
  return board

board = create_board()
board = drop(board, 1, 'X')
board = drop(board, 1, 'O')
board = drop(board, 2, 'X')
board = drop(board, 2, 'O')
board = drop(board, 2, 'X')
board = drop(board, 2, 'O')
board = drop(board, 2, 'X')
board = drop(board, 2, 'O')
board = drop(board, 2, 'X') # Full column
board = drop(board, 8, 'X') # Out of bounds
board = drop(board, 2, 'T') # Wrong piece
board = drop(board, 7, 'X')
print_board(board)