from cluster import *
import sys

class HierarchicalAlg:
	def __init__(self, distanceFunction):
		self.distanceFunc = distanceFunction
	
	def cluster(self, points):
		distances = []
		min = sys.maxint
		id1 = -1;
		id2 = -1;	
		
		for i in range(len(points)):
			print str(i)
			distances.append([])
			for j in range(i+1,len(points)):
				distances[i].insert(j, self.distanceFunc(points[i].vector, points[j].vector))
		while(len(points) > 1):
			print '3... remains ' + str(len(points))
			min = distances[0][1]
			id1 = 0
			id2 = 1
			for i in range(len(points)):
				for j in range(i+1,len(points)):
					if min > distances[i][j]:
						min = distances[i][j]
						id1 = i
						id2 = j
		
			newCluster = Cluster([points[id1], points[id2]])
			for i in range(len(points)):
				distances[i].remove(id2)
				points[i].vector.remove(id2)
			distances.remove(id2)
			points.remove(id2)
		
			points[id1] = newCluster
			for i in range(len(points)):
				distances[id1][i] = self.distanceFunc(points[i].vector, newCluster.vector)
				distances[i][id1] = distances[id1][i]
		return points			
