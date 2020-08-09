def render(board):
	width = len(board[0])
	top_border = '--'
	for x in range(width):
		top_border += '-'
	print(top_border)
	
	for row in range(len(board)):
		row_str = '|'
		for x in board[row]:
			if x == 0:
				row_str += 'o'
			elif x == 1:
				row_str += ' '
		row_str += '|'
		print(row_str)
		
	print(top_border)
	
