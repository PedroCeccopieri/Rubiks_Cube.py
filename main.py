import copy
from moves import *
from pieces import *
from cubeinput import *
from algorithms import *

print("""1 -> Verde
2 -> Vermelho
3 -> Azul
4 -> Laranja
5 -> Branco
6 -> Amarelo
A orientação sempre é com a face verde para frente e a branca para cima
""")

Cube = getCube()
CubeCopy = copy.deepcopy(Cube)

verifyCube(CubeCopy)
printCube(Cube)

