def checkmate(board_string):
   try:
      board = [list(row) for row in board_string.strip().split("\n")]
      size = len(board)
      for row in board:
            if len(row) != size:
               print("Error")
               return
                  
      king_pos = None

      for i in range(size):
            for j in range(size):
               if board[i][j] == 'K':
                  king_pos = (i, j)
                  break
               
      if not king_pos:
            print("Error")
            return

      rowK, colK = king_pos

      # Set up the directions that each piece can move
      directions = {
            'Q': [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)],
            'R': [(-1,0),(1,0),(0,-1),(0,1)],
            'B': [(-1,-1),(-1,1),(1,-1),(1,1)],
            'P': [(1,-1), (1,1)],
      }
      
      # Use the nested for-loops to iterate all the area in the board and find each piece.
      # Use outer loop to iterates the rows but in the inner loop iterate the columns.
      for piece, dirs in directions.items():
            for dx, dy in dirs:
               x, y = rowK + dx, colK + dy
               while 0 <= x < size and 0 <= y < size:
                  if board[x][y] == '.':
                        x += dx
                        y += dy
                  elif board[x][y] == piece or (piece == 'Q' and board[x][y] in ['Q']):
                        print("Success")
                        return
                  else:
                        break

      print("Fail")
   except:
      print("Error")
