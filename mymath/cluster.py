from Point import *

class Cluster(Point):
	def __init__(self, clusters):
		self.vector = []
		for i in range(len(clusters[0].vector)):
			self.vector.append(0)
		for i in range(len(clusters)):
			for j in range(len(clusters[i].vector)):
				self.vector[j] += clusters[i].vector[j]
		for i in range(len(self.vector)):
			self.vector[i] /= len(clusters)			
		self.clusters = clusters
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
