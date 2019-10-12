from algorithms import *
from moves import *
from cubeinput import printCube

# Cantos #

CGWO = [1, 4, 5] # Verde, Branco, Laranja #
CGWR = [1, 2, 5] # Verde, Branco, Vermelho #
CBWO = [3, 4, 5] # Azul, Branco, Laranja #
CBWR = [2, 3, 5] # Azul, Branco, Vermelho #

CGYO = [1, 4, 6] # Verde, Amarelo, Laranja #
CGYR = [1, 2, 6] # Verde, Amarelo, Vermelho #
CBYO = [3, 4, 6] # Azul, Amarelo, Laranja #
CBYR = [2, 3, 6] # Azul, Amarelo, Vermelho #

AllC = [CGWO, CGWR, CBWO, CBWR, CGYO, CGYR, CBYO, CBYR] # All Corners #

# Posiçao (x,y,z) dos cantos #
		   #z#		  #x#		 #y#
P125 = [[0, 0, 2], [1, 0, 0], [4, 2, 2]]
P126 = [[0, 2, 2], [1, 2, 0], [5, 0, 2]]																
P145 = [[0, 0, 0], [3, 0, 2], [4, 2, 0]]
P146 = [[0, 2, 0], [3, 2, 2], [5, 0, 0]]
P325 = [[2, 0, 0], [1, 0, 2], [4, 0, 2]]
P326 = [[2, 2, 0], [1, 2, 2], [5, 2, 2]] 
P345 = [[2, 0, 2], [3, 0, 0], [4, 0, 0]]
P346 = [[2, 2, 2], [3, 2, 0], [5, 2, 0]]

AllCP = [P125, P126, P145, P146, P325, P326, P345, P346] # Corners position 'x , y , z' #

# Meios #

EWG = [1, 5] # Verde, Branco #
EWR = [2, 5] # Vermelho, Branco #
EWB = [3, 5] # Azul, Branco #
EWO = [4, 5] # Laranja, Branco #

ERB = [2, 3] # Vermelho, Azul #
EOB = [3, 4] # Laranja, Azul #
ERG = [1, 2] # Vermelho, Verde #
EOG = [1, 4] # Laranja, Verde #

EYG = [1, 6] # Verde, Amarelo #
EYR = [2, 6] # Vermelho, Amarelo #
EYB = [3, 6] # Azul, Amarelo #
EYO = [4, 6] # Laranja, Amarelo #

AllE = [EWG, EWR, EWB, EWO, ERB, EOB, ERG, EOG, EYG, EYR, EYB, EYO] # All Edges #

P12 = [[0, 1, 2], [1, 1, 0]] ###0      # Top
P14 = [[0, 1, 0], [3, 1, 2]] ###1      ## Bottom
P15 = [[0, 0, 1], [4, 2, 1]] #2        ### Middle
P16 = [[0, 2, 1], [5, 0, 1]] ##3
P23 = [[1, 1, 2], [2, 1, 0]] ###4
P25 = [[1, 0, 1], [4, 1, 2]] #5
P26 = [[1, 2, 1], [5, 1, 2]] ##6
P34 = [[2, 1, 2], [3, 1, 0]] ###7
P35 = [[2, 0, 1], [4, 0, 1]] #8
P36 = [[2, 2, 1], [5, 2, 1]] ##9
P45 = [[3, 0, 1], [4, 1, 0]] #10
P46 = [[3, 2, 1], [5, 1, 0]] ##11

AllEP = [P12, P14, P15, P16, P23, P25, P26, P34, P35, P36, P45, P46] # Edges position 'x , y , z' #

def mSort(lista):

	for j in range(0, len(lista)):

		for k in range(j + 1, len(lista)):

			if (lista[j] > lista[k]):

				a = lista[j]
				lista[j] = lista[k]
				lista[k] = a

	return lista

def verifyPieces(Cube):

	C125 = [Cube[0][0][2], Cube[1][0][0], Cube[4][2][2]] # Verde, Branco, Vermelho  #
	C126 = [Cube[0][2][2], Cube[1][2][0], Cube[5][0][2]] # Verde, Amarelo, Vermelho #																
	C145 = [Cube[0][0][0], Cube[3][0][2], Cube[4][2][0]] # Verde, Branco, Laranja   #
	C146 = [Cube[0][2][0], Cube[3][2][2], Cube[5][0][0]] # Verde, Amarelo, Laranja  #
	C235 = [Cube[1][0][2], Cube[2][0][0], Cube[4][0][2]] # Azul, Branco, Vermelho   #
	C236 = [Cube[1][2][2], Cube[2][2][0], Cube[5][2][2]] # Azul, Amarelo, Vermelho  # 
	C345 = [Cube[2][0][2], Cube[3][0][0], Cube[4][0][0]] # Azul, Branco, Laranja    #
	C346 = [Cube[2][2][2], Cube[3][2][0], Cube[5][2][0]] # Azul, Amarelo, Laranja   #
														 #          Pos 			#

										 # 		 Pos 		 #
	E12 = [Cube[0][1][2], Cube[1][1][0]] # Verde, Vermelho   #
	E14 = [Cube[0][1][0], Cube[3][1][2]] # Verde, Laranja    #
	E15 = [Cube[0][0][1], Cube[4][2][1]] # Verde, Branco     #
	E16 = [Cube[0][2][1], Cube[5][0][1]] # Verde, Amarelo    #
	E23 = [Cube[1][1][2], Cube[2][1][0]] # Vermelho, Azul    #
	E25 = [Cube[1][0][1], Cube[4][1][2]] # Vermelho, Branco  #
	E26 = [Cube[1][2][1], Cube[5][1][2]] # Vermelho, Amarelo #
	E34 = [Cube[2][1][2], Cube[3][1][0]] # Laranja, Azul     #
	E35 = [Cube[2][0][1], Cube[4][0][1]] # Azul, Branco 	 #
	E36 = [Cube[2][2][1], Cube[5][2][1]] # Azul, Amarelo	 #
	E45 = [Cube[3][0][1], Cube[4][1][0]] # Laranja, Branco 	 #
	E46 = [Cube[3][2][1], Cube[5][1][0]] # Laranja, Amarelo  #
		
	AllCC = [C125, C126, C145, C146, C235, C236, C345, C346] # All corners coordinates #
	
	AllEC = [E12, E14, E15, E16, E23, E25, E26, E34, E35, E36, E45, E46] # All edges coordinates #

	countc = 0
	counte = 0

	for i in range(0, len(AllCC)):

		AllCC[i] = mSort(AllCC[i])

	for i in range(0, len(AllEC)):

		AllEC[i] = mSort(AllEC[i])

	# Verify Corners #
	for i in range(0, len(AllCC)):

		for j in range(0, len(AllC)):

			if (AllC[j] == AllCC[i]):

				countc += 1
	# Verify Edges #
	for i in range(0, len(AllEC)):

		for j in range(0, len(AllE)):

			if (AllE[j] == AllEC[i]):

				counte += 1

	if (counte == 12 and countc == 8):

		return True

	else:

		return False

def getCornersOrientation(Cube):

	orientation = []
	top = []
	botton = []

	ord1 = [2,0,4,6]
	for i in ord1:

		for j in range(3):

			a = AllCP[i][j][0]
			b = AllCP[i][j][1]
			c = AllCP[i][j][2]

			if (j == 2 and (Cube[a][b][c] == 5 or Cube[a][b][c] == 6)):

				top.append(1)

			if (j == 1 and (Cube[a][b][c] == 5 or Cube[a][b][c] == 6)):

				top.append(2)

			if (j == 0 and (Cube[a][b][c] == 5 or Cube[a][b][c] == 6)):

				top.append(3)

	ord2 = [3,1,5,7]
	for i in ord2:

		for j in range(3):

			a = AllCP[i][j][0]
			b = AllCP[i][j][1]
			c = AllCP[i][j][2]

			if (j == 2 and (Cube[a][b][c] == 5 or Cube[a][b][c] == 6)):

				botton.append(1)

			if (j == 1 and (Cube[a][b][c] == 5 or Cube[a][b][c] == 6)):

				botton.append(2)

			if (j == 0 and (Cube[a][b][c] == 5 or Cube[a][b][c] == 6)):

				botton.append(3)


	orientation.append(top)
	orientation.append(botton)

	return orientation

def verifyCorners(Cube):

	correct = [[1,1,1,1],[1,1,1,1]]
	u = 0
	d = 0
	
	while (True):

		corners = getCornersOrientation(Cube)

		if (corners == correct):

			return True

		elif (corners[0][0] == 2 and corners[0][3] == 2):

			fCase(Cube)

		elif (corners[0][0] == 3 and corners[0][3] == 3):

			eCase(Cube)

		elif (corners[0][1] == 3 and corners[0][2] == 2 and corners[0][3] == 3):

			sune(Cube)

		elif (corners[0][0] == 3 and corners[0][2] == 3 and corners[0][3] == 2):

			leftSune(Cube)

		elif (corners[0][0] == 3 and corners[0][2] == 2):

			back(Cube)
			eCase(Cube)
			backPrime(Cube)

		elif (corners[1][0] == 2 and corners[1][3] == 2):

			left2(Cube)
			fCase(Cube)
			left2(Cube)

		elif (corners[1][0] == 3 and corners[1][3] == 3):

			left2(Cube)
			eCase(Cube)
			left2(Cube)

		elif (corners[1][1] == 3 and corners[1][2] == 2 and corners[1][3] == 3):

			downLeftSune(Cube)

		elif (corners[1][0] == 3 and corners[1][2] == 3 and corners[1][3] == 2):

			downSune(Cube)

		elif (corners[0][0] == 3 and corners[0][2] == 2):

			backPrime(Cube)
			left2(Cube)
			eCase(Cube)
			left2(Cube)
			back(Cube)

		elif (corners[0][0] == 2 and corners[1][2] == 2):

			back2(Cube)
			fCase(Cube)
			back2(Cube)

		elif (corners[0][0] == 3 and corners[1][2] == 3):

			back2(Cube)
			eCase(Cube)
			back2(Cube)

		elif (corners[0][0] == 3 and corners[0][3] == 2 and corners[1][1] == 3):

			right2(Cube)
			leftSuneO(Cube)
			right2(Cube)

		elif (corners[0][3] == 3 and corners[1][1] == 2 and corners[1][2] == 3):

			right2(Cube)
			suneO(Cube)
			right2(Cube)

		else:

			if (u == 4):

				break

			elif (d == 4):

				u += 1
				d = 0
				up(Cube)

			else:

				d += 1
				down(Cube)

	return False

def getEdgesOrientation(Cube):

	orientation = []
	top = []
	middle = []
	bottom = []

	ord1 = [2,5,8,10]
	for i in ord1:

		piece = []
		rpiece = []

		for j in range(2):

			a = AllEP[i][j][0]
			b = AllEP[i][j][1]
			c = AllEP[i][j][2]

			piece.append(Cube[a][b][c])
			rpiece.append(Cube[a][b][c])

		piece = mSort(piece)

		if not (piece == ERB or piece == EOB or piece == ERG or piece == EOG):

			if not (rpiece[1] == 5 or rpiece[1] == 6):

				top.append([a,b,c])

		else:

			if not (rpiece[1] == 1 or rpiece[1] == 3):

				top.append([a,b,c])

	ord2 = [0,4,7,1]
	for i in ord2:

		piece = []
		rpiece = []

		if (i == 4):

			od = [1,0]
			for j in od:

				a = AllEP[i][j][0]
				b = AllEP[i][j][1]
				c = AllEP[i][j][2]

				piece.append(Cube[a][b][c])
				rpiece.append(Cube[a][b][c])

		else:

			for j in range(2):

				a = AllEP[i][j][0]
				b = AllEP[i][j][1]
				c = AllEP[i][j][2]

				piece.append(Cube[a][b][c])
				rpiece.append(Cube[a][b][c])

		piece = mSort(piece)

		if not (piece == ERB or piece == EOB or piece == ERG or piece == EOG):

			if not (rpiece[0] == 5 or rpiece[0] == 6):

				middle.append([a,b,c])

		else:

			if not (rpiece[0] == 1 or rpiece[0] == 3):

				middle.append([a,b,c])

	ord3 = [3,6,9,11]
	for i in ord3:

		piece = []
		rpiece = []

		for j in range(2):

			a = AllEP[i][j][0]
			b = AllEP[i][j][1]
			c = AllEP[i][j][2]

			piece.append(Cube[a][b][c])
			rpiece.append(Cube[a][b][c])

		piece = mSort(piece)

		if not (piece == ERB or piece == EOB or piece == ERG or piece == EOG):

			if not (rpiece[1] == 5 or rpiece[1] == 6):

				bottom.append([a,b,c])

		else:

			if not (rpiece[1] == 1 or rpiece[1] == 3):

				bottom.append([a,b,c])


	orientation.append(top)
	orientation.append(middle)
	orientation.append(bottom)
	
	return orientation

def verifyEdges(Cube):

	orientation = getEdgesOrientation(Cube)

	o = len(orientation[0]) + len(orientation[1]) + len(orientation[2])

	if (o % 2 == 0):

		return True

	else:

		return False

def verifyCube(Cube):

	print('Pieces:', verifyPieces(Cube))
	print('Corners:', verifyCorners(Cube))
	print('Edges:', verifyEdges(Cube))

