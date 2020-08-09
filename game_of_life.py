import sys

from render import render
from random_state import random_state, dead_state

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print(f'Usage: python {sys.argv[0]} width height', file=sys.stderr)
		sys.exit()
		
	arr = random_state(sys.argv[1], sys.argv[2])
	render(arr)
