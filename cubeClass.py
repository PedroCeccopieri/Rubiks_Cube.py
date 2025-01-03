import random

from pieces import *
from moves import *

colors = ("Verde", "Vermelha", "Azul", "Laranja", "Branca", "Amarela", "0", "1", "2", "3", "4", "5")

# All moves #
move1 = ('R', 'L', 'U', 'D', 'F', 'B', 'M', 'S', 'E', 'x', 'y', 'z', 'Rw', 'Lw', 'Uw', 'Dw', 'Fw', 'Bw')
move2 = ("R'", "L'", "U'", "D'", "F'", "B'", "M'", "S'", "E'", "x'", "y'", "z'", "Rw'", "Lw'", "Uw'", "Dw'", "Fw'", "Bw'")
move3 = ('R2', 'L2', 'U2', 'D2', 'F2', 'B2', 'M2', 'S2', 'E2', 'x2', 'y2', 'z2', 'Rw2', 'Lw2', 'Uw2', 'Dw2', 'Fw2', 'Bw2')

move = move1 + move2 + move3

class Cube:

    def __init__(self, s = ''):
        
        self.Cube = self.__getCube(state = s)


    def __getCube(self, state = ''):

        def getFace(x):

            face = []

            for i in range(3):

                linha = []

                for j in range(3):

                    if (i == 1 and j == 1):

                        color = x + 1

                    else:

                        color = input('(' + str(i) + ':' + str(j) + ')')

                        while (color not in colors):

                            print('Cor inválida!')
                            color = input('(' + str(i) + ':' + str(j) + ')')

                    linha.append(int(color))

                face.append(linha)

            return face

        cube = []

        if (state == '#'):

            cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], # U
                    [[1, 1, 1], [1, 1, 1], [1, 1, 1]], # L
                    [[2, 2, 2], [2, 2, 2], [2, 2, 2]], # F
                    [[3, 3, 3], [3, 3, 3], [3, 3, 3]], # R
                    [[4, 4, 4], [4, 4, 4], [4, 4, 4]], # B
                    [[5, 5, 5], [5, 5, 5], [5, 5, 5]]] # D
        else:

            for i in [4,3,0,1,2,5]:

                print('Face ' + colors[i] + ':')
                cube.append(getFace(i))

        return cube

    def printCube(self):

        for i in range(3):
            for j in range(9):

                print(end = ' ')

            print(self.Cube[0][i], end = '')
            print()

        for i in range(3):
            for j in range(1,5):

                print(self.Cube[j][i], end = '')

            print()

        for i in range(3):
            for j in range(9):

                print(end = ' ')

            print(self.Cube[5][i], end = '')
            print()
    # Return the color of the specific position #
    def getColor(self, pos):
        
        return self.Cube[pos[0]][pos[1]][pos[2]]
    # Return the position of a corner #
    def getCornerPos(self, color):

        for pos in AllCP:

            if (sorted(self.getCornerColor(pos)) == color):

                return pos
    # Return the position of a edge #
    def getEdgePos(self, color):

        for pos in AllEP:

            if (sorted(self.getEdgeColor(pos)) == color):

                return pos
    # Return the piece in a position #
    def getPieceColor(self, pos):

        return [self.Cube[col[0]][col[1]][col[2]] for col in pos]
    # Return all corners orientation #
    def getCornersOrientation(self):
        
        orientation = []
        top = []
        bottom = []

        facesOrientation = self.getCentersOrientation()
        faceUp = facesOrientation[0]
        faceDown = facesOrientation[5]

        for i in range(8):

            pos = AllCP[i]

            for idx, sticker in enumerate(pos):

                if (self.getColor(sticker) == faceUp or self.getColor(sticker) == faceDown):

                    if (idx < 4):
                        top.append(idx)
                    else:
                        bottom.append(idx)

        orientation.append(top)
        orientation.append(bottom)

        return orientation
    # Return all edges orientation #
    def getEdgesOrientation(self):

        orientation = []
        top = []
        middle = []
        bottom = []

        facesOrientation = self.getCentersOrientation()
        faceUp, faceDown = facesOrientation[0], facesOrientation[5]
        faceFront, faceBack = facesOrientation[2], facesOrientation[4]

        if (faceUp == 2 or faceDown == 2): pivot = [sorted(i) for i in [EWR, EWO, EYR, EYO]]
        elif (faceUp == 3 or faceDown == 3): pivot = [sorted(i) for i in [EYB, EWB, EYG, EWG]]
        elif (faceUp == 0 or faceDown == 0): pivot = [sorted(i) for i in [EBR, EBO, EGR, EGO]]

        for i in range(4):

            piece = (self.getColor(AllEP[i][0]), self.getColor(AllEP[i][1]))

            if not (sorted(piece) in pivot):

                if (piece[0] == faceUp or piece[0] == faceDown): top.append(1)
                else: top.append(2)

            else:

                if (piece[0] == faceFront or piece[0] == faceBack): top.append(1)
                else: top.append(2)

        for i in range(4,8):

            piece = (self.getColor(AllEP[i][0]), self.getColor(AllEP[i][1]))

            if not (sorted(piece) in pivot):

                if (piece[0] == faceUp or piece[0] == faceDown): middle.append(1)
                else: middle.append(2)

            else:

                if (piece[0] == faceFront or piece[0] == faceBack): middle.append(1)
                else: middle.append(2)

        for i in range(8,12):

            piece = (self.getColor(AllEP[i][0]), self.getColor(AllEP[i][1]))

            if not (sorted(piece) in pivot):

                if (piece[0] == faceUp or piece[0] == faceDown): bottom.append(1)
                else: bottom.append(2)

            else:

                if (piece[0] == faceFront or piece[0] == faceBack): bottom.append(1)
                else: bottom.append(2)

        orientation.append(top)
        orientation.append(middle)
        orientation.append(bottom)
        
        return orientation
    # Return all centers relative position #
    def getCentersOrientation(self):
        
        orientation = [self.getColor([i,1,1]) for i in range(6)] # ULFRBD #
        
        return orientation

    def doMoves(self):

        mvs = input('Insira os movimentos:').split(' ')
        done = False

        while not (done):
            for i in range (len(mvs)):

                if (mvs[i] not in move):

                    print ('Algum movimento inválido')
                    mvs = input('Insira os movimentos:').split(' ')
                    break

                else:

                    done = True

        self.read(mvs)
        self.printCube()

    def scramble(self):

        def complete(mvs):

            while not (len(mvs) >= 25):

                m = random.choice(move1[0:6] + move2[0:6] + move3[0:6])
                mvs.append(m)

            return mvs

        def remove(mvs):

            rmv = []

            for i in range(1,len(mvs)):

                if (mvs[i][0] == mvs[i - 1][0]):

                    rmv.append(i - 1)

            for i in reversed(rmv): mvs.pop(i)

            rmv.clear()

            for i in range(2, len(mvs)):

                if (mvs[i][0] == 'R' and mvs[i - 1][0] == 'L' and mvs[i - 2][0] == 'R'):

                    rmv.append(i - 2)

                if (mvs[i][0] == 'L' and mvs[i - 1][0] == 'R' and mvs[i - 2][0] == 'L'):

                    rmv.append(i - 2)

                if (mvs[i][0] == 'U' and mvs[i - 1][0] == 'D' and mvs[i - 2][0] == 'U'):

                    rmv.append(i - 2)

                if (mvs[i][0] == 'D' and mvs[i - 1][0] == 'U' and mvs[i - 2][0] == 'D'):

                    rmv.append(i - 2)

                if (mvs[i][0] == 'F' and mvs[i - 1][0] == 'B' and mvs[i - 2][0] == 'F'):

                    rmv.append(i - 2)

                if (mvs[i][0] == 'B' and mvs[i - 1][0] == 'F' and mvs[i - 2][0] == 'B'):

                    rmv.append(i - 2)

            for i in reversed(rmv): mvs.pop(i)

            return mvs

        scr = []

        while not (len(scr) == 25):

            scr = complete(scr)

            scr = remove(scr)

        print ('Scramble:')

        for i in scr:

            print (i, end = ' ')

        print()

        self.read(scr)

    def read(self, mvs):

        for i in mvs:

            match i:

                case 'R': right(self.Cube)
                case 'L': left(self.Cube)
                case 'U': up(self.Cube)
                case 'D': down(self.Cube) 
                case 'F': front(self.Cube)
                case 'B': back(self.Cube)
                case 'M': middle(self.Cube)
                case 'S': standing(self.Cube)
                case 'E': equatorial(self.Cube)
                case 'x': rotateCubeX(self.Cube)
                case 'y': rotateCubeY(self.Cube)
                case 'z': rotateCubeZ(self.Cube)
                case 'Rw': rightWide(self.Cube)
                case 'Lw': leftWide(self.Cube)
                case 'Uw': upWide(self.Cube)
                case 'Dw': downWide(self.Cube)
                case 'Fw': frontWide(self.Cube)
                case 'Bw': backWide(self.Cube)

                case "R'": rightPrime(self.Cube)
                case "L'": leftPrime(self.Cube)
                case "U'": upPrime(self.Cube)
                case "D'": downPrime(self.Cube) 
                case "F'": frontPrime(self.Cube)
                case "B'": backPrime(self.Cube)
                case "M'": middlePrime(self.Cube)
                case "S'": standingPrime(self.Cube) 
                case "E'": equatorialPrime(self.Cube)
                case "x'": rotateCubeXPrime(self.Cube)
                case "y'": rotateCubeYPrime(self.Cube)
                case "z'": rotateCubeZPrime(self.Cube)
                case "Rw'": rightWidePrime(self.Cube)
                case "Lw'": leftWidePrime(self.Cube)
                case "Uw'": upWidePrime(self.Cube)
                case "Dw'": downWidePrime(self.Cube)
                case "Fw'": frontWidePrime(self.Cube)
                case "Bw'": backWidePrime(self.Cube)

                case 'R2': right2(self.Cube)
                case 'L2': left2(self.Cube)
                case 'U2': up2(self.Cube)
                case 'D2': down2(self.Cube) 
                case 'F2': front2(self.Cube)
                case 'B2': back2(self.Cube)
                case 'M2': middle2(self.Cube)
                case 'S2': standing2(self.Cube) 
                case 'E2': equatorial2(self.Cube)
                case 'x2': rotateCubeX2(self.Cube)
                case 'y2': rotateCubeY2(self.Cube)
                case 'z2': rotateCubeZ2(self.Cube)
                case 'Rw2': rightWide2(self.Cube)
                case 'Lw2': leftWide2(self.Cube)
                case 'Uw2': upWide2(self.Cube)
                case 'Dw2': downWide2(self.Cube)
                case 'Fw2': frontWide2(self.Cube)
                case 'Bw2': backWide2(self.Cube)

    def printColors(self):

        def printLine(line):

            for color in line:
                
                match color:

                    case 0: print('\x1b[48;2;255;255;255m' + '  ' + '\x1b[0m' + ' ', end = '')
                    case 1: print('\x1b[48;2;255;163;0m' + '  ' + '\x1b[0m' + ' ', end = '')
                    case 2: print('\x1b[48;2;0;255;0m' + '  ' + '\x1b[0m' + ' ', end = '')
                    case 3: print('\x1b[48;2;255;0;0m' + '  ' + '\x1b[0m' + ' ', end = '')
                    case 4: print('\x1b[48;2;0;0;255m' + '  ' + '\x1b[0m' + ' ', end = '')
                    case 5: print('\x1b[48;2;255;255;0m' + '  ' + '\x1b[0m' + ' ', end = '')

        for i in range(3):
            for j in range(9):

                print(end = ' ')

            printLine(self.Cube[0][i])
            print()
            print()

        for i in range(3):
            for j in range(1,5):

                printLine(self.Cube[j][i])

            print()
            print()

        for i in range(3):
            for j in range(9):

                print(end = ' ')

            printLine(self.Cube[5][i])
            print()
            print()