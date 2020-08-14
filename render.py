# program to render board 
def render(board):
	# retrieve width
	width = len(board[0])
	
	# corner of board
	top_border = '--'
	
	# add in - for each cell
	for x in range(width):
		top_border += '-'
	# initially print top boarder
	print(top_border)
	
	# print inner board for each line
	for row in range(len(board)):
		# edge border
		row_str = '|'
		
		# if cell is dead, put blank space in board, if cell is alive put o
		for x in board[row]:
			if x == 0:
				row_str += ' '
			elif x == 1:
				row_str += 'o'
		# edge border
		row_str += '|'
		# print row
		print(row_str)
		
	# print bottom border
	print(top_border)
	
