nrows = 6
ncols = 7

def create_board(nrows, ncols):
  board = []
  for row in range(nrows):
    board_row = []
    for col in range(ncols):
      board_row.append(' ')
    board.append(board_row)
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

board = create_board(nrows, ncols)
print_board(board)