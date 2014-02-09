import sys
from math import *
from covariance import *

def minMaxN(points):
	n = MinMaxN(points)
	return n

def zScoreN(points):
	n = ZScoreN(points)
	return n

class Normalization():
	def normalizeDataSet(self, points, dim):
		pass
	def normalizePoint(self,point,dim):
		pass

class ZScoreN(Normalization):
	def __init__(self,points):
		self.initZScoreN(points)
	
	def initZScoreN(self, points):
		dimensions = len(points[0].vector)
		mean = Covariance.mean(points)
		stdev = [0] * dimensions
		for d in range(dimensions):
			for p in points:
				stdev[d] += pow(p.vector[d] - mean[d],2)
			stdev[d] = sqrt(stdev[d] / len(points))
		self.mean = mean
		self.stdev = stdev
		self.normalizeDataset(points)

	def normalizeDataset(self, points):
		for p in points:
			self.normalizePoint(p)

	def normalizePoint(self,p):
		v = p.vector
		dim = len(v)
		for d in range(dim):
			if self.stdev[d] == 0:
				continue
			v[d] = (v[d] - self.mean[d]) / float(self.stdev[d])


class MinMaxN(Normalization):
	def __init__(self, points):
		self.initMinMaxN(points)

	def initMinMaxN(self, points):
		dimensions = len(points[0].vector)
		self.min = [sys.maxint] * dimensions
		self.max = [-sys.maxint] * dimensions
		
		for p in points:
			for d in range(dimensions):
				if p.vector[d] > self.max[d]:
					self.max[d] = p.vector[d]
				if p.vector[d] < self.min[d]:
					self.min[d] = p.vector[d]	
		for p in points:
			self.normalizePoint(p)

	def normalizePoint(self, point):
		v = point.vector
		for i in range(len(v)):
			delta = float(self.max[i] - self.min[i])
			if delta == 0:
				continue
			v[i] = (v[i] - self.min[i]) /delta




