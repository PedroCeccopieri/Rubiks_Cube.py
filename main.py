from moves import *
from pieces import *
from algorithms import *
from verifier import verifyCube

from cubeClass import Cube

print("""1 -> Verde
2 -> Vermelho
3 -> Azul
4 -> Laranja
5 -> Branco
6 -> Amarelo
A orientação sempre é com a face verde para frente e a branca para cima
""")

cube = Cube()

verifyCube(cube)
#cube.printCube()
cube.scramble()
cube.printColors()