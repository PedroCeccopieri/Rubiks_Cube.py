# 0 -> 2
# 1 -> 3
# 2 -> 4
# 3 -> 1
# 4 -> 0
# 5 -> 5

def rotateFace(x, Cube):

	aux = Cube[x][0][0]
	Cube[x][0][0] = Cube[x][2][0]
	Cube[x][2][0] = Cube[x][2][2]
	Cube[x][2][2] = Cube[x][0][2]
	Cube[x][0][2] = aux

	aux2 = Cube[x][0][1]
	Cube[x][0][1] = Cube[x][1][0]
	Cube[x][1][0] = Cube[x][2][1]
	Cube[x][2][1] = Cube[x][1][2]
	Cube[x][1][2] = aux2

def rotateFacePrime(x, Cube):

	aux = Cube[x][0][0]
	Cube[x][0][0] = Cube[x][0][2]
	Cube[x][0][2] = Cube[x][2][2]
	Cube[x][2][2] = Cube[x][2][0]
	Cube[x][2][0] = aux

	aux2 = Cube[x][0][1]
	Cube[x][0][1] = Cube[x][1][2]
	Cube[x][1][2] = Cube[x][2][1]
	Cube[x][2][1] = Cube[x][1][0]
	Cube[x][1][0] = aux2

def right(Cube):
	# Permutação entre as faces #
	aux = Cube[0][0][2]
	aux2 = Cube[0][1][2]
	aux3 = Cube[0][2][2]

	Cube[0][0][2] = Cube[2][0][2]
	Cube[0][1][2] = Cube[2][1][2]
	Cube[0][2][2] = Cube[2][2][2]

	Cube[2][0][2] = Cube[5][0][2]
	Cube[2][1][2] = Cube[5][1][2]
	Cube[2][2][2] = Cube[5][2][2]

	Cube[5][0][2] = Cube[4][2][0]
	Cube[5][1][2] = Cube[4][1][0]
	Cube[5][2][2] = Cube[4][0][0]

	Cube[4][2][0] = aux
	Cube[4][1][0] = aux2
	Cube[4][0][0] = aux3
	
	rotateFace(3, Cube)
	
def left(Cube):

	aux = Cube[0][0][0]
	aux2 = Cube[0][1][0]
	aux3 = Cube[0][2][0]

	Cube[0][0][0] = Cube[4][2][2]
	Cube[0][1][0] = Cube[4][1][2]
	Cube[0][2][0] = Cube[4][0][2]

	Cube[4][2][2] = Cube[5][0][0]
	Cube[4][1][2] = Cube[5][1][0]
	Cube[4][0][2] = Cube[5][2][0]

	Cube[5][0][0] = Cube[2][0][0]
	Cube[5][1][0] = Cube[2][1][0]
	Cube[5][2][0] = Cube[2][2][0]

	Cube[2][0][0] = aux
	Cube[2][1][0] = aux2
	Cube[2][2][0] = aux3

	rotateFace(1, Cube)

def up(Cube):

	aux = Cube[1][0]

	Cube[1][0] = Cube[2][0]
	Cube[2][0] = Cube[3][0]
	Cube[3][0] = Cube[4][0]
	Cube[4][0] = aux

	rotateFace(0, Cube)

def down(Cube):

	aux = Cube[1][2]

	Cube[1][2] = Cube[4][2]
	Cube[4][2] = Cube[3][2]
	Cube[3][2] = Cube[2][2]
	Cube[2][2] = aux

	rotateFace(5, Cube)

def front(Cube):

	aux = Cube[3][0][0]
	aux2 = Cube[3][1][0]
	aux3 = Cube[3][2][0]

	Cube[3][0][0] = Cube[0][2][0]
	Cube[3][1][0] = Cube[0][2][1]
	Cube[3][2][0] = Cube[0][2][2]

	Cube[0][2][0] = Cube[1][2][2]
	Cube[0][2][1] = Cube[1][1][2]
	Cube[0][2][2] = Cube[1][0][2]

	Cube[1][2][2] = Cube[5][0][2]
	Cube[1][1][2] = Cube[5][0][1]
	Cube[1][0][2] = Cube[5][0][0]

	Cube[5][0][2] = aux
	Cube[5][0][1] = aux2
	Cube[5][0][0] = aux3

	rotateFace(2, Cube)

def back(Cube):

	aux = Cube[3][0][2]
	aux2 = Cube[3][1][2]
	aux3 = Cube[3][2][2]

	Cube[3][0][2] = Cube[5][2][2]
	Cube[3][1][2] = Cube[5][2][1]
	Cube[3][2][2] = Cube[5][2][0]

	Cube[5][2][2] = Cube[1][2][0]
	Cube[5][2][1] = Cube[1][1][0]
	Cube[5][2][0] = Cube[1][0][0]

	Cube[1][2][0] = Cube[0][0][0]
	Cube[1][1][0] = Cube[0][0][1]
	Cube[1][0][0] = Cube[0][0][2]

	Cube[0][0][0] = aux
	Cube[0][0][1] = aux2
	Cube[0][0][2] = aux3

	rotateFace(4, Cube)

def middle(Cube):
	
	aux = Cube[0][0][1]
	aux2 = Cube[0][1][1]
	aux3 = Cube[0][2][1]

	Cube[0][0][1] = Cube[4][2][1]
	Cube[0][1][1] = Cube[4][1][1]
	Cube[0][2][1] = Cube[4][0][1]

	Cube[4][2][1] = Cube[5][0][1]
	Cube[4][1][1] = Cube[5][1][1]
	Cube[4][0][1] = Cube[5][2][1]

	Cube[5][0][1] = Cube[2][0][1]
	Cube[5][1][1] = Cube[2][1][1]
	Cube[5][2][1] = Cube[2][2][1]

	Cube[2][0][1] = aux
	Cube[2][1][1] = aux2
	Cube[2][2][1] = aux3

def standing(Cube):

	aux = Cube[0][1][0]
	aux2 = Cube[0][1][1]
	aux3 = Cube[0][1][2]

	Cube[0][1][0] = Cube[1][2][1]
	Cube[0][1][1] = Cube[1][1][1]
	Cube[0][1][2] = Cube[1][0][1]

	Cube[1][0][1] = Cube[5][1][0]
	Cube[1][1][1] = Cube[5][1][1]
	Cube[1][2][1] = Cube[5][1][2]

	Cube[5][1][0] = Cube[3][2][1]
	Cube[5][1][1] = Cube[3][1][1]
	Cube[5][1][2] = Cube[3][0][1]

	Cube[3][0][1] = aux
	Cube[3][1][1] = aux2
	Cube[3][2][1] = aux3

def equatorial(Cube):
	
	aux = Cube[2][1]

	Cube[2][1] = Cube[1][1]

	Cube[1][1] = Cube[4][1]

	Cube[4][1] = Cube[3][1]

	Cube[3][1] = aux

def rotateCubeX(Cube):

	aux = Cube[2]

	Cube[2] = Cube[5]
	Cube[5] = Cube[4]
	Cube[4] = Cube[0]
	Cube[0] = aux

	rotateFace(3,Cube)
	rotateFacePrime(1,Cube)
	for i in range(2):
		rotateFace(4,Cube)
		rotateFace(5,Cube)

def rotateCubeY(Cube):

	aux = Cube[2]

	Cube[2] = Cube[3]
	Cube[3] = Cube[4]
	Cube[4] = Cube[1]
	Cube[1] = aux

	rotateFace(0,Cube)
	rotateFacePrime(5,Cube)

def rotateCubeZ(Cube):

	aux = Cube[0]

	Cube[0] = Cube[1]
	Cube[1] = Cube[5]
	Cube[5] = Cube[3]
	Cube[3] = aux

	for i in [0,1,2,3,5]:
		rotateFace(i,Cube)
	rotateFacePrime(4,Cube)

def rightWide(Cube):

	right(Cube)
	middlePrime(Cube)

def leftWide(Cube):

	left(Cube)
	middle(Cube)

def upWide(Cube):

	up(Cube)
	equatorialPrime(Cube)

def downWide(Cube):

	down(Cube)
	equatorial(Cube)

def frontWide(Cube):

	front(Cube)
	standing(Cube)

def backWide(Cube):

	back(Cube)
	standingPrime(Cube)

def right2(Cube):

	for i in range (2):
		right(Cube)

def left2(Cube):

	for i in range (2):
		left(Cube)

def up2(Cube):

	for i in range (2):
		up(Cube)

def down2(Cube):

	for i in range (2):
		down(Cube)

def front2(Cube):

	for i in range (2):
		front(Cube)

def back2(Cube):

	for i in range (2):
		back(Cube)

def middle2(Cube):
	
	for i in range(2):
		middle(Cube)

def standing2(Cube):
	
	for i in range(2):
		standing(Cube)

def equatorial2(Cube):
	
	for i in range(2):
		equatorial(Cube)

def rotateCubeX2(Cube):

	for i in range(2):
		rotateCubeX(Cube)

def rotateCubeY2(Cube):

	for i in range(2):
		rotateCubeY(Cube)

def rotateCubeZ2(Cube):

	for i in range(2):
		rotateCubeZ(Cube)

def rightWide2(Cube):

	for i in range(2):
		rightWide(Cube)

def leftWide2(Cube):

	for i in range(2):
		leftWide(Cube)

def upWide2(Cube):

	for i in range(2):
		upWide(Cube)

def downWide2(Cube):

	for i in range(2):
		downWide(Cube)

def frontWide2(Cube):

	for i in range(2):
		frontWide(Cube)

def backWide2(Cube):

	for i in range(2):
		backWide(Cube)

def rightPrime(Cube):

	aux = Cube[0][0][2]
	aux2 = Cube[0][1][2]
	aux3 = Cube[0][2][2]

	Cube[0][0][2] = Cube[4][2][0]
	Cube[0][1][2] = Cube[4][1][0]
	Cube[0][2][2] = Cube[4][0][0]

	Cube[4][2][0] = Cube[5][0][2]
	Cube[4][1][0] = Cube[5][1][2]
	Cube[4][0][0] = Cube[5][2][2]

	Cube[5][0][2] = Cube[2][0][2]
	Cube[5][1][2] = Cube[2][1][2]
	Cube[5][2][2] = Cube[2][2][2]

	Cube[2][0][2] = aux
	Cube[2][1][2] = aux2
	Cube[2][2][2] = aux3
	
	rotateFacePrime(3, Cube)

def leftPrime(Cube):

	aux = Cube[0][0][0]
	aux2 = Cube[0][1][0]
	aux3 = Cube[0][2][0]

	Cube[0][0][0] = Cube[2][0][0]
	Cube[0][1][0] = Cube[2][1][0]
	Cube[0][2][0] = Cube[2][2][0]

	Cube[2][0][0] = Cube[5][0][0]
	Cube[2][1][0] = Cube[5][1][0]
	Cube[2][2][0] = Cube[5][2][0]

	Cube[5][0][0] = Cube[4][2][2]
	Cube[5][1][0] = Cube[4][1][2]
	Cube[5][2][0] = Cube[4][0][2]

	Cube[4][2][2] = aux
	Cube[4][1][2] = aux2
	Cube[4][0][2] = aux3

	rotateFacePrime(1, Cube)

def upPrime(Cube):

	aux = Cube[1][0]

	Cube[1][0] = Cube[4][0]
	Cube[4][0] = Cube[3][0]
	Cube[3][0] = Cube[2][0]
	Cube[2][0] = aux

	rotateFacePrime(0, Cube)

def downPrime(Cube):

	aux = Cube[1][2]

	Cube[1][2] = Cube[2][2]
	Cube[2][2] = Cube[3][2]
	Cube[3][2] = Cube[4][2]
	Cube[4][2] = aux

	rotateFacePrime(5, Cube)

def frontPrime(Cube):

	aux = Cube[3][0][0]
	aux2 = Cube[3][1][0]
	aux3 = Cube[3][2][0]

	Cube[3][0][0] = Cube[5][0][2]
	Cube[3][1][0] = Cube[5][0][1]
	Cube[3][2][0] = Cube[5][0][0]

	Cube[5][0][2] = Cube[1][2][2]
	Cube[5][0][1] = Cube[1][1][2]
	Cube[5][0][0] = Cube[1][0][2]

	Cube[1][2][2] = Cube[0][2][0]
	Cube[1][1][2] = Cube[0][2][1]
	Cube[1][0][2] = Cube[0][2][2]

	Cube[0][2][0] = aux
	Cube[0][2][1] = aux2
	Cube[0][2][2] = aux3

	rotateFacePrime(2, Cube)

def backPrime(Cube):

	aux = Cube[3][0][2]
	aux2 = Cube[3][1][2]
	aux3 = Cube[3][2][2]

	Cube[3][0][2] = Cube[0][0][0]
	Cube[3][1][2] = Cube[0][0][1]
	Cube[3][2][2] = Cube[0][0][2]

	Cube[0][0][0] = Cube[1][2][0]
	Cube[0][0][1] = Cube[1][1][0]
	Cube[0][0][2] = Cube[1][0][0]

	Cube[1][2][0] = Cube[5][2][2]
	Cube[1][1][0] = Cube[5][2][1]
	Cube[1][0][0] = Cube[5][2][0]

	Cube[5][2][2] = aux
	Cube[5][2][1] = aux2
	Cube[5][2][0] = aux3

	rotateFacePrime(4, Cube)

def middlePrime(Cube):
	
	aux = Cube[0][0][1]
	aux2 = Cube[0][1][1]
	aux3 = Cube[0][2][1]

	Cube[0][0][1] = Cube[2][0][1]
	Cube[0][1][1] = Cube[2][1][1]
	Cube[0][2][1] = Cube[2][2][1]

	Cube[2][0][1] = Cube[5][0][1]
	Cube[2][1][1] = Cube[5][1][1]
	Cube[2][2][1] = Cube[5][2][1]

	Cube[5][0][1] = Cube[4][2][1]
	Cube[5][1][1] = Cube[4][1][1]
	Cube[5][2][1] = Cube[4][0][1]

	Cube[4][2][1] = aux
	Cube[4][1][1] = aux2
	Cube[4][0][1] = aux3

def standingPrime(Cube):
		
	aux = Cube[0][1][0]
	aux2 = Cube[0][1][1]
	aux3 = Cube[0][1][2]

	Cube[0][1][0] = Cube[3][0][1]
	Cube[0][1][1] = Cube[3][1][1]
	Cube[0][1][2] = Cube[3][2][1]

	Cube[3][0][1] = Cube[5][1][2]
	Cube[3][1][1] = Cube[5][1][1]
	Cube[3][2][1] = Cube[5][1][0]

	Cube[5][1][0] = Cube[1][0][1]
	Cube[5][1][1] = Cube[1][1][1]
	Cube[5][1][2] = Cube[1][2][1]

	Cube[1][2][1] = aux
	Cube[1][1][1] = aux2
	Cube[1][0][1] = aux3

def equatorialPrime(Cube):
	
	aux = Cube[2][1]

	Cube[2][1] = Cube[3][1]

	Cube[3][1] = Cube[4][1]

	Cube[4][1] = Cube[1][1]

	Cube[1][1] = aux

def rotateCubeXPrime(Cube):

	aux = Cube[2]

	Cube[2] = Cube[0]
	Cube[0] = Cube[4]
	Cube[4] = Cube[5]
	Cube[5] = aux

	rotateFace(1,Cube)
	rotateFacePrime(3,Cube)
	for i in range(2):
		rotateFace(4,Cube)
		rotateFace(0,Cube)

def rotateCubeYPrime(Cube):

	aux = Cube[2]

	Cube[2] = Cube[1]
	Cube[1] = Cube[4]
	Cube[4] = Cube[3]
	Cube[3] = aux

	rotateFace(5,Cube)
	rotateFacePrime(0,Cube)

def rotateCubeZPrime(Cube):

	aux = Cube[0]

	Cube[0] = Cube[3]
	Cube[3] = Cube[5]
	Cube[5] = Cube[1]
	Cube[1] = aux

	rotateFace(2,Cube)
	for i in [0,1,2,3,5]:
		rotateFacePrime(i,Cube)

def rightWidePrime(Cube):

	rightPrime(Cube)
	middle(Cube)

def leftWidePrime(Cube):

	leftPrime(Cube)
	middlePrime(Cube)

def upWidePrime(Cube):

	upPrime(Cube)
	equatorial(Cube)

def downWidePrime(Cube):

	downPrime(Cube)
	equatorialPrime(Cube)

def frontWidePrime(Cube):

	frontPrime(Cube)
	standingPrime(Cube)

def backWidePrime(Cube):

	backPrime(Cube)
	standing(Cube)