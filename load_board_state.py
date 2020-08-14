import sys
from random_state import dead_state
from render import render

def split(word):
	return [char for char in word]

def load_board_state(textfile):
	try:
		f = open(textfile, 'r')
		data = f.readlines()
		data = [x.strip() for x in data]
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		
	load_board = dead_state(len(data[0]), len(data))
	
	height_index = 0
	
	while height_index < len(data):
		width_index = 0
		while width_index < len(data[0]):
			load_board[height_index][width_index] = int(data[height_index][width_index])
			width_index += 1
		height_index += 1

	return load_board
	
if __name__ == '__main__':
	load_board_state(sys.argv[1])
