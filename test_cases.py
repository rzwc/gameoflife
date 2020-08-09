from next_board_state import next_board_state

if __name__ == "__main__":
	# Test 1: dead cells with no live neighbours
	# should stay dead
	
	init_state1 = [
		[0,0,0],
		[0,0,0],
		[0,0,0]
	]
	
	expected_next_state1 = [
		[0,0,0],
		[0,0,0],
		[0,0,0]
	]
	
	actual_next_state1 = next_board_state(init_state1, 3, 3)
	
	if expected_next_state1 == actual_next_state1:
		print("PASSED 1")
	else:
		print("FAILED 1")
		print("Expected:")
		print(expected_next_state1)
		print("Actual:")
		print(actual_next_state1)
		
	# Test 2: dead cells with exactly 3 neighbours	
	# should come out alive
	
	init_state2 = [
		[0,0,1],
		[0,1,1],
		[0,0,0]
	]
	
	expected_next_state2 = [
		[0,1,1],
		[0,1,1],
		[0,0,0]
	]
	
	actual_next_state2 = next_board_state(init_state2, 3, 3)
	
	if expected_next_state2 == actual_next_state2:
		print("PASSED 2")
	else:
		print("FAILED 2")
		print("Expected:")
		print(expected_next_state2)
		print("Actual:")
		print(actual_next_state2)
		
