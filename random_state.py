# Program to initiate random or dead state for board 
import sys

import random 

# create random state of board with alive and dead cells
def random_state(width, height):
	
	# create empty board with heigh and width
	arr = dead_state(width, height)
	
	height_index = 0
	width_index = 0
	
	# loop through every cell and assign an alive or dead 
	while height_index < len(arr):
		while width_index < len(arr[height_index]):
			# random number between 0-1
			random_number = random.random()
			# 50% chance for cell to be dead or alive
			if random_number >= 0.5:
				cell_state = 0
			else:
				cell_state = 1
				
			# assign cell state 
			arr[height_index][width_index] = cell_state
			width_index += 1
		width_index = 0
		height_index += 1
		
	return arr
	
# create empty board with all dead cells
def dead_state(width, height):
	
	arr = [[0 for i in range(int(width))] for j in range(int(height))]
	
	return arr

if __name__ == "__main__":
	
	# Usage
	if len(sys.argv) != 3:
		print(f'Usage: python {sys.argv[0]} width height', file=sys.stderr)
		sys.exit()
	
	# render board
	render(random_state(sys.argv[1],sys.argv[2]))
	
	
