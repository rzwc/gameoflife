# program used to determine the next board state using game of life rules
from random_state import dead_state

def next_board_state(board):

	# retrieve width and height from board
	width = len(board[0])
	height = len(board)

	# create new board to store next state
	nextboard = dead_state(width, height)
	
	# loop through each cell and determine next state by looking at neighbours
	for x in range(0, height):
		for y in range(0, width):
			# receive current cell value, 1 or 2
			current_cell_value = board[x][y]
			# initialize/reset neighbour variable
			neighbours = 0
			
			# corner case
			if x == 0 and y == 0 or x == 0 and y == (width-1) or x == (height-1) and y == 0 or x == (height-1) and y == (width-1):
			
				# if top left corner, check neighbours, increment neighbours if found
				if x == 0 and y == 0:
					if board[x][y+1] == 1:
						neighbours += 1
					if board[x+1][y] == 1:
						neighbours += 1
					if board[x+1][y+1] == 1:
						neighbours += 1
						
				# if top right corner, check neighbours, increment neighbours if found
				if x == 0 and y == (width-1):
					if board[x][y-1] == 1:
						neighbours += 1
					if board[x+1][y] == 1:
						neighbours += 1
					if board[x-1][y-1] == 1:
						neighbours += 1
						
				# if bottom left corner, check neighbours, increment neighbours if found	
				if x == (height-1) and y == 0:
					if board[x][y+1] == 1:
						neighbours += 1
					if board[x-1][y] == 1:
						neighbours += 1
					if board[x-1][y+1] == 1:
						neighbours += 1
						
				# if bottom right corner, check neighbours, increment neighbours if found		
				if x == (height-1) and y == (width-1):
					if board[x][y-1] == 1:
						neighbours += 1
					if board[x-1][y] == 1:
						neighbours += 1
					if board[x-1][y-1] == 1:
						neighbours += 1
					
				# if current cell is alive	
				if board[x][y] == 1:
					# 0 or 1 neighbours, underpopulation, current cell dies
					if neighbours == 0 or neighbours == 1:
						nextboard[x][y] = 0
					# 2 or 3 neighbours, neighbourhood is right, current cell stays alive
					elif neighbours == 2 or neighbours == 3:
						nextboard[x][y] = 1
					# more than 3 neighbours, overpopulation, current cell dies
					elif neighbours > 3:
						nextboard[x][y] = 0
				# if current cell is dead
				elif board[x][y] == 0:
					# 3 neighbours, neighbourhood is just right, current cell becomes alive
					if neighbours == 3:
						nextboard[x][y] = 1
						
			# edge cases that are not corners
			# check if cell is at the edge
			elif x == 0 or x == (height-1) or y == 0 or y == (width-1):
				# if top edge
				# check neighbours and increment if found
				if x == 0:
					for i in range(x, x+2):
						for j in range(y-1, y+2):
							if board[i][j] == 1:
								neighbours += 1
				# if bottom edge
				# check neighbours and increment if found
				if x == (height-1):
					for i in range(x-1, x+1):
						for j in range(y-1, y+2):
							if board[i][j] == 1:
								neighbours += 1
				# if left edge
				# check neighbours and increment if found
				if y == 0:
					for i in range(x-1, x+2):
						for j in range(y, y+2):
							if board[i][j] == 1:
								neighbours += 1
				# if right edge
				# check neighbours and increment if found		
				if y == (width-1):
					for i in range(x-1, x+2):
						for j in range(y-1, y+1):
							if board[i][j] == 1:
								neighbours += 1
				# if current cell is alive	
				if board[x][y] == 1:
					# subtract counting self as neighbour
					neighbours -= 1
					# 0 or 1 neighbours, underpopulation, current cell dies
					if neighbours == 0 or neighbours == 1:
						nextboard[x][y] = 0
					# 2 or 3 neighbours, neighbourhood is right, current cell stays alive
					elif neighbours == 2 or neighbours == 3:
						nextboard[x][y] = 1
					# more than 3 neighbours, overpopulation, current cell dies
					elif neighbours > 3:
						nextboard[x][y] = 0
				# if current cell is dead
				elif board[x][y] == 0:
					# 3 neighbours, neighbourhood is just right, current cell becomes alive
					if neighbours == 3:
						nextboard[x][y] = 1
						
			else: 
				# check inner cells for neighbours, increment neighbours if found
				for i in range(x-1, x+2):
					for j in range(y-1, y+2):
						if board[i][j] == 1:
							neighbours += 1
				# if current cell is alive	
				if board[x][y] == 1:
					# subtract counting self as neighbour
					neighbours -= 1
					# 0 or 1 neighbours, underpopulation, current cell dies
					if neighbours == 0 or neighbours == 1:
						nextboard[x][y] = 0
					# 2 or 3 neighbours, neighbourhood is right, current cell stays alive
					elif neighbours == 2 or neighbours == 3:
						nextboard[x][y] = 1
					# more than 3 neighbours, overpopulation, current cell dies
					elif neighbours > 3:
						nextboard[x][y] = 0
				# if current cell is dead
				elif board[x][y] == 0:
					# 3 neighbours, neighbourhood is just right, current cell becomes alive
					if neighbours == 3:
						nextboard[x][y] = 1
	
	# return next board	
	return nextboard
