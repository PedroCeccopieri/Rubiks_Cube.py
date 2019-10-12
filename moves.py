from cubeinput import printCube
import random

move = ('r', 'l', 'u', 'd', 'f', 'b', 'r2', 'l2', 'u2', 'd2', 'f2', 'b2', "r'", "l'", "u'", "d'", "f'", "b'")

def rotateFace(x, Cube):

	aux = Cube[x][0][2]

	Cube[x][0][2] = Cube[x][0][0]
	Cube[x][0][0] = Cube[x][2][0]
	Cube[x][2][0] = Cube[x][2][2]
	Cube[x][2][2] = aux

	aux2 = Cube[x][1][2]

	Cube[x][1][2] = Cube[x][0][1]
	Cube[x][0][1] = Cube[x][1][0]
	Cube[x][1][0] = Cube[x][2][1]
	Cube[x][2][1] = aux2

def rotateFacePrime(x, Cube):

	aux = Cube[x][0][2]

	Cube[x][0][2] = Cube[x][2][2]
	Cube[x][2][2] = Cube[x][2][0]
	Cube[x][2][0] = Cube[x][0][0]
	Cube[x][0][0] = aux

	aux2 = Cube[x][1][2]

	Cube[x][1][2] = Cube[x][2][1]
	Cube[x][2][1] = Cube[x][1][0]
	Cube[x][1][0] = Cube[x][0][1]
	Cube[x][0][1] = aux2

def right(Cube):
	# Permutação entre as faces #
	aux = Cube[4][0][2]
	aux2 = Cube[4][1][2]
	aux3 = Cube[4][2][2]

	Cube[4][0][2] = Cube[0][0][2]
	Cube[4][1][2] = Cube[0][1][2]
	Cube[4][2][2] = Cube[0][2][2]

	Cube[0][0][2] = Cube[5][0][2]
	Cube[0][1][2] = Cube[5][1][2]
	Cube[0][2][2] = Cube[5][2][2]

	Cube[5][0][2] = Cube[2][2][0]
	Cube[5][1][2] = Cube[2][1][0]
	Cube[5][2][2] = Cube[2][0][0]

	Cube[2][2][0] = aux
	Cube[2][1][0] = aux2
	Cube[2][0][0] = aux3
	
	rotateFace(1, Cube)
	
def left(Cube):

	aux = Cube[4][0][0]
	aux2 = Cube[4][1][0]
	aux3 = Cube[4][2][0]

	Cube[4][0][0] = Cube[2][2][2]
	Cube[4][1][0] = Cube[2][1][2]
	Cube[4][2][0] = Cube[2][0][2]

	Cube[2][2][2] = Cube[5][0][0]
	Cube[2][1][2] = Cube[5][1][0]
	Cube[2][0][2] = Cube[5][2][0]

	Cube[5][0][0] = Cube[0][0][0]
	Cube[5][1][0] = Cube[0][1][0]
	Cube[5][2][0] = Cube[0][2][0]

	Cube[0][0][0] = aux
	Cube[0][1][0] = aux2
	Cube[0][2][0] = aux3

	rotateFace(3, Cube)

def up(Cube):

	aux = Cube[3][0]

	Cube[3][0] = Cube[0][0]
	Cube[0][0] = Cube[1][0]
	Cube[1][0] = Cube[2][0]
	Cube[2][0] = aux

	rotateFace(4, Cube)

def down(Cube):

	aux = Cube[3][2]

	Cube[3][2] = Cube[2][2]
	Cube[2][2] = Cube[1][2]
	Cube[1][2] = Cube[0][2]
	Cube[0][2] = aux

	rotateFace(5, Cube)

def front(Cube):

	aux = Cube[1][0][0]
	aux2 = Cube[1][1][0]
	aux3 = Cube[1][2][0]

	Cube[1][0][0] = Cube[4][2][0]
	Cube[1][1][0] = Cube[4][2][1]
	Cube[1][2][0] = Cube[4][2][2]

	Cube[4][2][0] = Cube[3][2][2]
	Cube[4][2][1] = Cube[3][1][2]
	Cube[4][2][2] = Cube[3][0][2]

	Cube[3][2][2] = Cube[5][0][2]
	Cube[3][1][2] = Cube[5][0][1]
	Cube[3][0][2] = Cube[5][0][0]

	Cube[5][0][2] = aux
	Cube[5][0][1] = aux2
	Cube[5][0][0] = aux3

	rotateFace(0, Cube)

def back(Cube):

	aux = Cube[1][0][2]
	aux2 = Cube[1][1][2]
	aux3 = Cube[1][2][2]

	Cube[1][0][2] = Cube[5][2][2]
	Cube[1][1][2] = Cube[5][2][1]
	Cube[1][2][2] = Cube[5][2][0]

	Cube[5][2][2] = Cube[3][2][0]
	Cube[5][2][1] = Cube[3][1][0]
	Cube[5][2][0] = Cube[3][0][0]

	Cube[3][2][0] = Cube[4][0][0]
	Cube[3][1][0] = Cube[4][0][1]
	Cube[3][0][0] = Cube[4][0][2]

	Cube[4][0][0] = aux
	Cube[4][0][1] = aux2
	Cube[4][0][2] = aux3

	rotateFace(2, Cube)

def right2(Cube):

	for i in range (0, 2):

		right(Cube)

def left2(Cube):

	for i in range (0, 2):

		left(Cube)

def up2(Cube):

	for i in range (0, 2):

		up(Cube)

def down2(Cube):

	for i in range (0, 2):

		down(Cube)

def front2(Cube):

	for i in range (0, 2):

		front(Cube)

def back2(Cube):

	for i in range (0, 2):

		back(Cube)

def rightPrime(Cube):

	aux = Cube[4][0][2]
	aux2 = Cube[4][1][2]
	aux3 = Cube[4][2][2]

	Cube[4][0][2] = Cube[2][2][0]
	Cube[4][1][2] = Cube[2][1][0]
	Cube[4][2][2] = Cube[2][0][0]

	Cube[2][2][0] = Cube[5][0][2]
	Cube[2][1][0] = Cube[5][1][2]
	Cube[2][0][0] = Cube[5][2][2]

	Cube[5][0][2] = Cube[0][0][2]
	Cube[5][1][2] = Cube[0][1][2]
	Cube[5][2][2] = Cube[0][2][2]

	Cube[0][0][2] = aux
	Cube[0][1][2] = aux2
	Cube[0][2][2] = aux3
	
	rotateFacePrime(1, Cube)

def leftPrime(Cube):

	aux = Cube[4][0][0]
	aux2 = Cube[4][1][0]
	aux3 = Cube[4][2][0]

	Cube[4][0][0] = Cube[0][0][0]
	Cube[4][1][0] = Cube[0][1][0]
	Cube[4][2][0] = Cube[0][2][0]

	Cube[0][0][0] = Cube[5][0][0]
	Cube[0][1][0] = Cube[5][1][0]
	Cube[0][2][0] = Cube[5][2][0]

	Cube[5][0][0] = Cube[2][2][2]
	Cube[5][1][0] = Cube[2][1][2]
	Cube[5][2][0] = Cube[2][0][2]

	Cube[2][2][2] = aux
	Cube[2][1][2] = aux2
	Cube[2][0][2] = aux3

	rotateFacePrime(3, Cube)

def upPrime(Cube):

	aux = Cube[3][0]

	Cube[3][0] = Cube[2][0]
	Cube[2][0] = Cube[1][0]
	Cube[1][0] = Cube[0][0]
	Cube[0][0] = aux

	rotateFacePrime(4, Cube)

def downPrime(Cube):

	aux = Cube[3][2]

	Cube[3][2] = Cube[0][2]
	Cube[0][2] = Cube[1][2]
	Cube[1][2] = Cube[2][2]
	Cube[2][2] = aux

	rotateFacePrime(5, Cube)

def frontPrime(Cube):

	aux = Cube[1][0][0]
	aux2 = Cube[1][1][0]
	aux3 = Cube[1][2][0]

	Cube[1][0][0] = Cube[5][0][2]
	Cube[1][1][0] = Cube[5][0][1]
	Cube[1][2][0] = Cube[5][0][0]

	Cube[5][0][2] = Cube[3][2][2]
	Cube[5][0][1] = Cube[3][1][2]
	Cube[5][0][0] = Cube[3][0][2]

	Cube[3][2][2] = Cube[4][2][0]
	Cube[3][1][2] = Cube[4][2][1]
	Cube[3][0][2] = Cube[4][2][2]

	Cube[4][2][0] = aux
	Cube[4][2][1] = aux2
	Cube[4][2][2] = aux3

	rotateFacePrime(0, Cube)

def backPrime(Cube):

	aux = Cube[1][0][2]
	aux2 = Cube[1][1][2]
	aux3 = Cube[1][2][2]

	Cube[1][0][2] = Cube[4][0][0]
	Cube[1][1][2] = Cube[4][0][1]
	Cube[1][2][2] = Cube[4][0][2]

	Cube[4][0][0] = Cube[3][2][0]
	Cube[4][0][1] = Cube[3][1][0]
	Cube[4][0][2] = Cube[3][0][0]

	Cube[3][2][0] = Cube[5][2][2]
	Cube[3][1][0] = Cube[5][2][1]
	Cube[3][0][0] = Cube[5][2][0]

	Cube[5][2][2] = aux
	Cube[5][2][1] = aux2
	Cube[5][2][0] = aux3

	rotateFacePrime(2, Cube)

def read(mvs, Cube):

	for i in range (0, len(mvs)):

		if (mvs[i].lower() == 'r'):

			right(Cube)

		elif (mvs[i].lower() == 'l'):

			left(Cube)

		elif (mvs[i].lower() == 'u'):

			up(Cube)

		elif (mvs[i].lower() == 'd'):

			down(Cube)

		elif (mvs[i].lower() == 'f'):

			front(Cube)

		elif (mvs[i].lower() == 'b'):

			back(Cube)

		elif (mvs[i].lower() == 'r2'):

			right2(Cube)

		elif (mvs[i].lower() == 'l2'):

			left2(Cube)

		elif (mvs[i].lower() == 'u2'):

			up2(Cube)

		elif (mvs[i].lower() == 'd2'):

			down2(Cube)

		elif (mvs[i].lower() == 'f2'):

			front2(Cube)

		elif (mvs[i].lower() == 'b2'):

			back2(Cube)

		elif (mvs[i].lower() == "r'"):

			rightPrime(Cube)

		elif (mvs[i].lower() == "l'"):

			leftPrime(Cube)

		elif (mvs[i].lower() == "u'"):

			upPrime(Cube)

		elif (mvs[i].lower() == "d'"):

			downPrime(Cube)

		elif (mvs[i].lower() == "f'"):

			frontPrime(Cube)

		elif (mvs[i].lower() == "b'"):

			backPrime(Cube)

def doMoves(Cube):

	mvs = input('Insira os movimentos:').split(',')
	a = True

	while (a):

		for i in range (0, len(mvs)):

			if (mvs[i] not in move):

				print ('Algum movimento inválido')
				mvs = input('Insira os movimentos:').split(',')
				break

			else:

				a = False

	read(mvs, Cube)

	printCube(Cube)

def scramble(Cube):

	def complete(mvs):

		while not (len(mvs) >= 25):

			a = random.choice(move)

			if not (a.isnumeric()):

				mvs.append(a)

		return mvs

	def remove(mvs):

		rmv = []

		for i in range(len(mvs)):

			if (i > 0 and mvs[i][0] == mvs[i - 1][0]):

				rmv.append(i - 1)

		rmv.reverse()

		for i in rmv:

			mvs.pop(i)

		rmv.clear()

		for i in range(len(mvs)):

			if (i > 2 and mvs[i][0] == 'r' and mvs[i - 1][0] == 'l' and mvs[i - 2][0] == 'r'):

				rmv.append(i - 2)

			if (i > 2 and mvs[i][0] == 'l' and mvs[i - 1][0] == 'r' and mvs[i - 2][0] == 'l'):

				rmv.append(i - 2)

			if (i > 2 and mvs[i][0] == 'u' and mvs[i - 1][0] == 'd' and mvs[i - 2][0] == 'u'):

				rmv.append(i - 2)

			if (i > 2 and mvs[i][0] == 'd' and mvs[i - 1][0] == 'u' and mvs[i - 2][0] == 'd'):

				rmv.append(i - 2)

			if (i > 2 and mvs[i][0] == 'f' and mvs[i - 1][0] == 'b' and mvs[i - 2][0] == 'f'):

				rmv.append(i - 2)

			if (i > 2 and mvs[i][0] == 'b' and mvs[i - 1][0] == 'f' and mvs[i - 2][0] == 'b'):

				rmv.append(i - 2)

		rmv.reverse()

		for i in rmv:

			mvs.pop(i)

		return mvs

	alo = []

	while not (len(alo) == 25):

		alo = complete(alo)

		alo = remove(alo)

	print ('Scramble:')

	for i in alo:

		print (i, end = ' ')

	read(alo, Cube)
