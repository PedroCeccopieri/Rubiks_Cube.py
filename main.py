import os

from moves import *
from pieces import *
from algorithms import *
from verifier import verifyCube
# from dr import *
from comutators import *

from cubeClass import Cube

os.system("")

print("""0 -> Branco
1 -> Laranja
2 -> Verde
3 -> Vermelho
4 -> Azul
5 -> Amarelo
A orientação sempre é com a face verde para frente e a branca para cima
""")

cube = Cube(s = '#')

verifyCube(cube)
cube.scramble()


cube.printColors()