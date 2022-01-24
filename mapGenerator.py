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
	for column in range(len(tileMap)):
		for tile in range(len(tileMap[column])):
			tileMap[column][tile] = random.randint(0,1)

# Pass in finished array as argument, then display level
def displayMap(completeLevel):

	for i in range (len(completeLevel)):
		print(completeLevel[i])

	random.randint(0,1)


# Create a level that has equal dimensions length and height, then randomly pick tiles to be placed in the level.
def main():

	sizeOfLevel = 4
	level = generateBlankTileMap(sizeOfLevel)

	# Randomly select tiles to be place in the level
	pickTiles(level)
	# Print out the finished level generation
	displayMap(level)
main()