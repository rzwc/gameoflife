from random_state import dead_state

def next_board_state(board, width, height):

	nextboard = dead_state(width, height)
	
	for x in range(0, height):
		for y in range(0, width):
			current_cell_value = board[x][y]
			neighbours = 0
			if x == 0 and y == 0 or x == 0 and y == (width-1) or x == (height-1) and y == 0 or x == (height-1) and y == (width-1):
				board[x][y] == 0
			elif x == 0 or x == (height-1) or y == 0 or y == (width-1):
				board[x][y] == 0
			else: 
				for i in range(x-1, x+2):
					for j in range(y-1, y+2):
						if board[i][j] == 1:
							neighbours += 1
			
				if board[x][y] == 1:
					if neighbours == 0 or neighbours == 1:
						nextboard[x][y] = 0
					elif neighbours == 2 or neighbours == 3:
						nextboard[x][y] = 1
					elif neighbours > 3:
						nextboard[x][y] = 0
				elif board[x][y] == 0:
					if neighbours == 3:
						nextboard[x][y] = 1
				
	return nextboard
