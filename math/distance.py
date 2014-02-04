import math

def check(v1,v2):
	if(len(v1) != len(v2))
		raise ValueError("size of v1 != size of v2")

def euclideanDistance(v1, v2):
	d = 0
	for i in range(len(v1)):
		d += pow(v1[i] - v2[i], 2)
	d = sqrt(d)
	return d


def mahalanobisDistance(v1,v2):
	check(v1,v2)
	pass
	
def cosineDistance(v1,v2):
	check(v1,v2)
	d = 0
	v1Sqr = 0
	v2Sqr = 0
	for i in range(len(v1)):
		d += v1[i] * v2[i]
		v1Sqr += pow(v1[i],2)
		v2Sqr += pow(v1[i],2)
	v1Sqr = sqrt(v1Sqr)
	v2Sqr = sqrt(v2Sqr)
	d /= (v1Sqr * v2Sqr)
	return d

def manhattanDistance(v1,v2):
	check(v1,v2)
	d = 0
	for i in range(len(v1)):
		d += abs(v1[i] - v2[i])
	return d
def mikowskiDistance(v1,v2):
	check(v1,v2)
	d = 0
	p = 1.5
	for i in range(len(v1)):
		d += pow(abs(v1[i]-v2[i]),p)
	return d
	