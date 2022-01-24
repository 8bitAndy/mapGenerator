import random

# Create the blank level of whatever user specified size. Creates a 2D array and returns that to main
def generateBlankTileMap(levelSize):
	level = []


	for i in range(levelSize):
		#print("this is loop", i)
		level.append([])
		for x in range(levelSize):
			level[i].append(0)


	return level


# Function loops through entire 2D array and randomly picks a number for each tile
def pickTiles(tileMap):
	# Check if level starting point has been placed
	startPlaced = False
	endPlaced = False
	ableToFinishLevel = False

	# Used to check which row is being currently checked in the 2D array
	currentRow = 0

	# Add starting tile to map
	if startPlaced == False:
		startPlaced = True
		tileMap[0][0] = 8

	# Add ending tile to map
	if endPlaced == False:
		endPlaced = True
		tileMap[-1][-1] = 9

	# Keep regenerating the level until it can be finished
	while ableToFinishLevel == False:
		# Loop through arrays and randomly choose tiles to be placed
		for row in range(len(tileMap)):
			for column in range(len(tileMap[row])):
				# Used to signify if a tile should be placed
				spawnTile = False

				# Check that a tile is empty, a tile is empty if it contains 0 as a value
				if tileMap[row][column] == 0:

					# Check if tile to the left of the current one has anything in it, if it does then we can potentially generate a tile
					if (tileMap[row][column - 1] != 0 and tileMap[row][column - 1] != 9) and spawnTile == False:
						spawnTile = True

					# Check the tile above to see if there is anything there
					if currentRow != 0 and tileMap[row - 1][column] != 0:
						spawnTile = True

					# If one or more conditions are met then spawn a tile in the current position
					if spawnTile == True:
						tileMap[row][column] = random.randint(0,1)

			# Increment the current row by one to keep track of which row we are spawning tiles in
			currentRow+= 1

		# Check if level finish is connected above
		if tileMap[-2][-1] !=0:
			ableToFinishLevel = True

		# Check if level finish is connected by a tile to the left
		if tileMap[-1][-2] != 0:
			ableToFinishLevel = True

	print("The level can be finished?",ableToFinishLevel)

# Pass in finished array as argument, then display level
def displayMap(completeLevel):

	for i in range (len(completeLevel)):
		print(completeLevel[i])

	random.randint(0,1)


# Create a level that has equal dimensions length and height, then randomly pick tiles to be placed in the level.
def main():

	sizeOfLevel = 10

	level = generateBlankTileMap(sizeOfLevel)

	# Randomly select tiles to be place in the level
	pickTiles(level)
	# Print out the finished level generation
	displayMap(level)
main()