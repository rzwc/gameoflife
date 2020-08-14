# main program used to run game of life
import sys

from os import system, name
from time import sleep
from render import render
from random_state import random_state, dead_state
from next_board_state import next_board_state
from load_board_state import load_board_state

# function used to clear the command line console to 'refresh' pattern
def clear():
	
	# check if windows
	if name == 'nt':
		_ = system('cls')
	# if mac or linux
	else:
		_ = system('clear')

if __name__ == "__main__":

	# Usage 
	if len(sys.argv) != 3 and len(sys.argv) != 2:
		print(f'Usage: python {sys.argv[0]} premadeboard', file=sys.stderr)
		print(f'Usage: python {sys.argv[0]} width height', file=sys.stderr)
		sys.exit()
	
	# if width and height are inputted
	if len(sys.argv) == 3:	
		
		# create random state of board
		arr = random_state(sys.argv[1], sys.argv[2])
		
		#render board
		render(arr)
		
		# infinite loop
		while True:
			
			# retrieve next board state, render board, pause for 0.2 sec, clear board
			arr = next_board_state(arr)
			render(arr)	
			sleep(0.2) 
			clear()
			
	# if premade board is inputted
	if len(sys.argv) == 2:
	
		# load board, store loaded board in arr and render board
		loaded_board = load_board_state(sys.argv[1])
		arr = loaded_board
		render(arr)
		
		# infinite loop
		while True:
		
			# retrieve next board state, render board, pause for 0.2 sec, clear board
			arr = next_board_state(arr)
			render(arr)
			sleep(0.2)
			clear()
	
