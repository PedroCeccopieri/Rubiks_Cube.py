from pieces import AllCC, AllCP, AllEC, AllEP

# Verify if all pieces exist #
def verifyPieces(cube):

	ver = 0

	cor = [tuple(sorted(cube.getCornerColor(i))) for i in AllCP]

	if (sorted(cor) == sorted(list(AllCC))): ver += 1

	edg = [tuple(sorted(cube.getEdgesColor(i))) for i in AllEP]

	if (sorted(edg) == sorted(list(AllEC))): ver += 1

	return ver == 2
# Verify if all corners can be orientate #
def verifyCorners(cube):

	corners = cube.getCornersOrientation()
	
	verification = 0
	
	for idx, ori in enumerate(corners[0] + corners[1]):
		
		if ((idx % 2 == 0 and idx < 4) or (idx % 2 == 1 and idx >= 4)):

			match ori:

				case 2: verification += 1
				case 3: verification += 2

		else:

			match ori:

				case 2: verification += 2
				case 3: verification += 1

	return verification % 3 == 0
# Verify if all edges can be orientate #
def verifyEdges(cube):

	orientation = cube.getEdgesOrientation()

	orienteds = (orientation[0] + orientation[1] + orientation[2]).count(1)

	return orienteds % 2 == 0
# Verify the Pieces, Corners and Edges #
def verifyCube(cube):

	print('Pieces:', verifyPieces(cube))
	print('Corners:', verifyCorners(cube))
	print('Edges:', verifyEdges(cube))
