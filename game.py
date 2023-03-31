import os

nrows = 6
ncols = 7
pieces = ['X', 'O']

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def create_board():
  board = []
  for row in range(nrows):
    board_row = []
    for col in range(ncols):
      board_row.append(' ')
    board.append(board_row)
  print_board(board)
  return board

def print_board(board):
  cls()
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
  # if piece not in pieces:
  #   print("Enter valid piece: X or O.")
  #   return board

  col -= 1
  for row in range(len(board)-1,-1,-1):
    if board[row][col] == ' ':
      board[row][col] = piece
      break
    elif row == 0:
      print("Column full. Choose other column.")
  print_board(board)
  return board

def is_valid(ncol, row0):
  if ncol < 1 or ncol > ncols:
    print("Enter valid column.")
    return False
  if row0[ncol - 1] != ' ':
    print("Column full. Enter other column.")
    return False
  return True

def has_won(board, piece):
  # Horizontal
  for row in range(len(board)-1, -1, -1):
    count = 0
    for col in range(len(board[row])):
      if board[row][col] == piece:
        count += 1
      else:
        count = 0      
      if count == 4:
        print("{PIECE} has won!".format(PIECE=piece))
        return True

  # Vertical
  for col in range(len(board[0])):
    counter = 0
    for row in range(len(board)-1, -1, -1):
      if board[row][col] == piece:
        count += 1
      else:
        count = 0
      if count == 4:
        print("{PIECE} has won!".format(PIECE=piece))
        return True

  # / - Diagonal
  for row in range(len(board)-1, 2, -1):
    for col in range(len(board[row])-3):
      if [board[row][col],board[row - 1][col + 1], board[row - 2][col + 2],board[row - 3][col + 3]].count(piece) == 4:
        print("{PIECE} has won!".format(PIECE=piece))
        return True
  # \ - Diagonal
  for row in range(len(board)-1, 2, -1):
    for col in range(3, len(board[row])):
      if [board[row][col],board[row - 1][col - 1],board[row - 2][col - 2],board[row - 3][col - 3]].count(piece) == 4:
        print("{PIECE} has won!".format(PIECE=piece))
        return True
  # Default
  return False

def is_full(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == ' ':
        return False
  print("It's a tie!")
  return True

def is_end(board):
  return has_won(board, 'X') or has_won(board, 'O') or is_full(board)

def play():
  # Initialize board
  board = create_board()

  # Initialize turn
  turn = 'X'

  # Loop game
  while (not is_end(board)):
    col = int(input("{TURN}'s turn - Enter column index: ".format(TURN=turn)))
    while (not is_valid(col, board[0])):
      col = int(input("{TURN}'s turn - Enter column index: ".format(TURN=turn)))

    board = drop(board, col, turn)

    # Switch turn
    if turn == 'X':
      turn = 'O'
    else:
      turn = 'X'
  else:
    print("Game has ended!")

play()