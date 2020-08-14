import sys
from random_state import dead_state
from render import render

def load_board_state(textfile):

	# open text file, store lines in data and strip \n 
	try:
		f = open(textfile, 'r')
		data = f.readlines()
		data = [x.strip() for x in data]
	# IOError exception
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		
	# create empty board use dimensions from text file
	load_board = dead_state(len(data[0]), len(data))
	
	# index to track height of board
	height_index = 0
	
	# loop through height and width and set the empty board equal to the integers in the text file
	while height_index < len(data):
		width_index = 0
		while width_index < len(data[0]):
			load_board[height_index][width_index] = int(data[height_index][width_index])
			width_index += 1
		height_index += 1

	return load_board
