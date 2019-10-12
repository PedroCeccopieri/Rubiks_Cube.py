from moves import *
from cubeinput import printCube

r, l, u, d, f, b = 'r', 'l', 'u', 'd', 'f', 'b'
rl, ll, ul, dl, fl, bl = "r'", "l'", "u'", "d'", "f'", "b'"
r2, l2, u2, d2, f2, b2 = 'r2', 'l2', 'u2', 'd2', 'f2', 'b2'

def pllU(Cube):

	mvs = [rl,u,rl,ul,rl,ul,rl,u,r,u,r2]

	read(mvs, Cube)

def pllUP(Cube):

	mvs = [r2,ul,rl,ul,r,u,r,u,r,ul,r]

	read(mvs, Cube)

def pllDownU(Cube):

	mvs = [ll,d,ll,dl,ll,dl,ll,d,l,d,l2]

	read(mvs, Cube)

def pllDownUP(Cube):

	mvs = [l2,dl,ll,dl,l,d,l,d,l,dl,l]

	read(mvs, Cube)

def sune(Cube):

	mvs = [r,u,rl,u,r,u2,rl]

	read(mvs, Cube)

def suneO(Cube):

	sune(Cube)
	up(Cube)
	pllUP(Cube)
	up(Cube)

def leftSune(Cube):

	mvs = [ll,ul,l,ul,ll,u2,l]

	read(mvs, Cube)

def leftSuneO(Cube):

	leftSune(Cube)
	upPrime(Cube)
	pllU(Cube)
	upPrime(Cube)

def antiSune(Cube):

	mvs = [r,u2,rl,ul,r,ul,rl]

	read(mvs, Cube)

def leftAntiSune(Cube):

	mvs = [ll,u2,l,u,ll,u,l]

	read(mvs, Cube)

def downSune(Cube):

	mvs = [l,d,ll,d,l,d2,ll]

	read(mvs, Cube)

def downSuneO(Cube):

	downSune(Cube)
	down(Cube)
	pllDownUP(Cube)
	down(Cube)

def downLeftSune(Cube):

	mvs = [rl,dl,r,dl,rl,d2,r]

	read(mvs, Cube)

def downLeftSuneO(Cube):

	downLeftSune(Cube)
	downPrime(Cube)
	pllDownU(Cube)
	downPrime(Cube)

def eCase(Cube):

	sune(Cube)
	leftSune(Cube)

def fCase(Cube):

	leftAntiSune(Cube)
	antiSune(Cube)
