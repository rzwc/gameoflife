import sys

from os import system, name
from time import sleep
from render import render
from random_state import random_state, dead_state
from next_board_state import next_board_state
from load_board_state import load_board_state

def clear():
	
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

if __name__ == "__main__":

	if len(sys.argv) != 3 and len(sys.argv) != 2:
		print(f'Usage: python {sys.argv[0]} premadeboard', file=sys.stderr)
		print(f'Usage: python {sys.argv[0]} width height', file=sys.stderr)
		sys.exit()
	
	if len(sys.argv) == 3:	
	
		arr = random_state(sys.argv[1], sys.argv[2])
		render(arr)
		
		while True:
			arr = next_board_state(arr)
			render(arr)	
			sleep(0.2) 
			clear()
	if len(sys.argv) == 2:
	
		loaded_board = load_board_state(sys.argv[1])
		arr = loaded_board
		render(arr)
		
		while True:
			arr = next_board_state(arr)
			render(arr)
			sleep(0.2)
			clear()
	
