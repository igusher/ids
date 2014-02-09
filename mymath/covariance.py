from numpy import matrix

class Covariance():

	@classmethod
	def mean(cls, points):
		if hasattr(Covariance, 'means'):
			return Covariance.means
		metricNum = len(points[0].vector)
		pointsNum = len(points)
		covMatrix = []
		means = [0]*metricNum
		for metric in range(metricNum):
			means.append(0)
			for point in points:
				means[metric] += point.vector[metric]
			means[metric] /= float(pointsNum)
		Covariance.means = means
		return means
	
	@classmethod
	def calcCovariance(cls, points):
		metricNum = len(points[0].vector)
		pointsNum = len(points)
		means = Covariance.mean(points)	
		sum = 0
		covMatrix = [[0]*metricNum]*metricNum
		for mx in range(metricNum):
			for my in range(mx,metricNum):
				sum = 0
				for point in points:
					sum += (point.vector[mx] - means[mx]) * (point.vector[my] - means[my])
				sum /= float(pointsNum-1)
				covMatrix[mx][my] = sum
				covMatrix[my][mx] = sum
			
		Covariance.covMatrix = matrix(covMatrix)
		Covariance.means = means
		return Covariance.covMatrix
		
