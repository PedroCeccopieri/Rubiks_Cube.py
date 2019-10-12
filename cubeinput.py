colors = ("Verde", "Vermelha", "Azul", "Laranja", "Branca", "Amarela", "1", "2", "3", "4", "5", "6")

def getFace(x):

	face = []

	for i in range (0, 3):

		linha = []

		for j in range (0, 3):

			if (i == 1 and j == 1):

				color = x + 1

			else:

				color = input('(' + str(i + 1) + ':' + str(j + 1) + ')')

				while (color not in colors):

					print ('Cor inválida!')
					color = input('(' + str(i + 1) + ':' + str(j + 1) + ')')

			linha.append(int(color))

		face.append(linha)

	return face

def getCube():

	cube = []
	chose = input()

	if (chose == '#'):

		cube = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 
				[[2, 2, 2], [2, 2, 2], [2, 2, 2]], 
				[[3, 3, 3], [3, 3, 3], [3, 3, 3]], 
				[[4, 4, 4], [4, 4, 4], [4, 4, 4]], 
				[[5, 5, 5], [5, 5, 5], [5, 5, 5]], 
				[[6, 6, 6], [6, 6, 6], [6, 6, 6]]]
	else:

		for i in range (0, 6):

			print ('Face ' + colors[i] + ':')
			cube.append(getFace(i))

	return cube

def printCube(Cube):

	for i in range (0, 3):

		for j in range (0, 9):

			print (end = ' ')

		print (Cube[4][i], end = '')
		print ()

	for i in range (0, 3):

		print (Cube[3][i], end = '')
		print (Cube[0][i], end = '')
		print (Cube[1][i], end = '')
		print (Cube[2][i], end = '')
		print ()

	for i in range (0, 3):

		for j in range (0, 9):

			print (end = ' ')

		print (Cube[5][i], end = '')
		print ()