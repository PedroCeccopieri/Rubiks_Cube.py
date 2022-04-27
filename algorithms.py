from moves import *

def pllU(cube):

	mvs = "R' U R' U' R' U' R' U R U R2"
	cube.read(mvs.split(' '))

def pllUP(cube):

	mvs = "R2 U' R' U' R U R U R U' R"
	cube.read(mvs.split(' '))

def pllUDown(cube):

	mvs = "L' D L' D' L' D' L' D L D L2"
	cube.read(mvs.split(' '))

def pllUPDown(cube):

	mvs = "L2 D' L' D' L D L D L D' L"
	cube.read(mvs.split(' '))

def sune(cube):

	mvs = "R U R' U R U2 R'"
	cube.read(mvs.split(' '))

def suneO(cube):

	mvs = "R U R' U R U2 R' U R2 U' R' U' R U R U R U' R U"
	cube.read(mvs.split(' '))

def leftSune(cube):

	mvs = "L' U' L U' L' U2 L"
	cube.read(mvs.split(' '))

def leftSuneO(cube):

	mvs = "L' U' L U' L' U2 L U' R' U R' U' R' U' R' U R U R2 U'"
	cube.read(mvs.split(' '))

def antiSune(cube):

	mvs = "R U2 R' U' R U' R'"
	cube.read(mvs.split(' '))

def leftAntiSune(cube):

	mvs = "L' U2 L U L' U L"
	cube.read(mvs.split(' '))

def downSune(cube):

	mvs = "L D L' D L D2 L'"
	cube.read(mvs.split(' '))

def downSuneO(cube):

	mvs = "L D L' D L D2 L' D L2 D' L' D' L D L D L D' L D"
	cube.read(mvs.split(' '))

def downLeftSune(cube):

	mvs = "R' D' R D' R D2 R"
	cube.read(mvs.split(' '))

def downLeftSuneO(cube):

	mvs = "R' D' R D' R D2 R D' L' D L' D' L' D' L' D L D L2 D'"
	cube.read(mvs.split(' '))

def eCase(cube):

	mvs = "R U R' U R U2 R' L' U' L U' L' U2 L"
	cube.read(mvs.split(' '))

def fCase(cube):

	mvs = "L' U2 L U L' U L R U2 R' U' R U' R'"
	cube.read(mvs.split(' '))
