import random, sys

mazeSize = 15
if len(sys.argv)>1:
	mazeSize = int(sys.argv[1])*2+1
maxIntWalls = 0
if len(sys.argv)>2:
	maxIntWalls = int(sys.argv[2])

def initMaze(): 
	maze = emptymaze(maxIntWalls)
	return generateMaze(maze)

def emptymaze(interiorWallsCnt):
	maze = []
	for i in range(mazeSize):
		line = []
		for j in range(mazeSize):
			line.append(i==0 or i== mazeSize-1 or j==0 or j == mazeSize-1)
		maze.append(line)
	for i in range(interiorWallsCnt):
		maze[random.randint(0, mazeSize//2)*2][random.randint(0, mazeSize//2)*2]=1
	return maze

def generateMaze(maze):
	walls = getavailabelwalls(maze)
	while(len(walls)>0):
		index = random.randint(0,len(walls)-1)
		wall = walls[index]
		newwalls = possiblewalls(maze,wall)
		if len(newwalls) == 0:
			walls.pop(index)
		else:
			newwall = newwalls[random.randint(0,len(newwalls)-1)]
			maze[newwall['x']][newwall['y']] = 1
			maze[(newwall['x']+wall['x'])//2][(newwall['y']+wall['y'])//2] = 1
			walls.append(newwall)
	# put entrance and exit on top and bottom wall
	maze[0][random.randint(1, mazeSize//2)*2 -1] = 0
	maze[mazeSize-1][random.randint(1, mazeSize//2)*2 -1] = 0
	return maze

def getavailabelwalls(maze):
	walls = []
	for i in range(mazeSize//2 +1):
		for j in range(mazeSize//2 +1):
			if maze[i*2][j*2]:
				walls.append({"x":i*2,"y":j*2})
	return walls

def possiblewalls(maze,wall):
	up = {"x":wall['x']-2, "y":wall['y']}
	down = {"x":wall['x']+2, "y":wall['y']}
	left = {"x":wall['x'], "y":wall['y']-2}
	right = {"x":wall['x'], "y":wall['y']+2}
	newwalls = []
	if up['x']>=0 and not maze[up['x']][up['y']]:
		newwalls.append(up)
	if down['x']<mazeSize and not maze[down['x']][down['y']]:
		newwalls.append(down)
	if left['y']>=0 and not maze[left['x']][left['y']]:
		newwalls.append(left)
	if right['y']<mazeSize and not maze[right['x']][right['y']]:
		newwalls.append(right)
	return newwalls

def printMaze(maze):
	for lines in maze:
		strLine = ''
		for block in lines:
			if(block):
				strLine += "█"
			else:
				strLine += " "
		print(strLine)

maze = initMaze()
printMaze(maze)