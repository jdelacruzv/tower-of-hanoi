NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1

rods = {
    'A': range(NUMBER_OF_DISKS, 0, -1),
    'B': [],
    'C': []
}

def move():
	print(rods)