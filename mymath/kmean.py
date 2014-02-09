import sys
from cluster import *
from clusterNonEucl import *

class Kmean:
	def __init__(self, testpoints, distanceFunc):
		self.distanceFunc = distanceFunc
		self.clusters = {}
		for k in list(testpoints.keys()):
			newCluster = Cluster(testpoints[k])
			#newCluster = ClusterNonEucl(testpoints[k])
			self.clusters[k] = newCluster

	def findClosestCluster(self, point):
		min = sys.maxint
		clusterName = '-1'
		for k,v in self.clusters.iteritems():
			d = self.distanceFunc(point.vector, v.vector)
			if min > d:
				min = d
				clusterName = k
		return clusterName

	def findClosestByRadius(self, point):
		min = sys.maxint
		clusterName = '-1'
		for k,v in self.clusters.iteritems():
			d = v.calcRadius(point)
			if min > d:
				min = d
				clusterName = k
		return clusterName

	def addPoint(self, point):
		cluster = self.findClosestCluster(point)
		cluster.addPoint(point)
		return cluster
			
		
