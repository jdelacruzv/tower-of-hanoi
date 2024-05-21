NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1

rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def move(n, source, auxiliary, target):
	# Display starting configuration
	for i in range(0, number_of_moves):
		remainder = (i + 1) % 3
		if remainder == 1:
			print(f'Move {i + 1} allowed between {source} and {target}')
		elif remainder == 2:
			print(f'Move {i + 1} allowed between {source} and {auxiliary}')
	print(rods)

# Initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
