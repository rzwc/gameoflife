import sys

import random 

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
				row_str += '.'
		row_str += '|'
		print(row_str)
		
	print(top_border)
	

def random_state(width, height):
	arr = dead_state(width, height)
	
	height_index = 0
	width_index = 0
	while height_index < len(arr):
		while width_index < len(arr[height_index]):
			random_number = random.random()
			if random_number >= 0.5:
				cell_state = 0
			else:
				cell_state = 1
			arr[height_index][width_index] = cell_state
			width_index += 1
		width_index = 0
		height_index += 1
		
	return arr
	
def dead_state(width, height):
	
	# WRONG arr = [[0]*int(width)]*int(height)
	arr = [[0 for i in range(int(width))] for j in range(int(height))]
	
	return arr

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print(f'Usage: python {sys.argv[0]} width height', file=sys.stderr)
		sys.exit()
	
	render(random_state(sys.argv[1],sys.argv[2]))
	
