from Point import *
from mymath.distance import *
import sys

class ClusterNonEucl(Point):
	def __init__(self, clusters):
		self.clusters = clusters
#		self.vector = self.findClustroid()	
		
	def findClustroid(self):
		minRadius = sys.maxint
		clustroid = []
		for point in self.clusters:
			rad = self.calcRadius(point)
			if rad < minRadius:
				minRadius = rad
				clustroid = point.vector
		return clustroid
	
	def calcRadius(self,point):
		radius = 0
		distanceFunc = manhattanDistance 
		for cluster in self.clusters:
			radius += distanceFunc(point.vector, cluster.vector)	
		radius /= float(len(self.clusters))
		return radius
	
	def append(self, cluster):
		self.clusters.append(clusters)
	def addPoint(self, point):
		for i in range(len(self.vector)):
			self.vector[i] = (self.vector[i] * len(self.clusters) + point.vector[i]) / (len(self.clusters) + 1) 
	def getId(self):
		ids = []
		for cluster in self.clusters:
			ids.append(cluster.getId())
		return ids
