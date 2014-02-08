from capturemodel.CaptureSource import *
from Point import Point
from mymath.distance import *
from mymath.hierarchical import *
from mymath.kmean import *
from mymath.covariance import *
import os 

#distanceFunc = euclideanDistance
#distanceFunc = mahalanobisDistance
distanceFunc = manhattanDistance

headersFile = 'resources/test_capture_head'
#trainingDataFile = 'resources/test_capture_back'
trainingDataFile = 'resources/test_capture'
#testDataFile = 'resources/test_capture_back'
testDataFile = 'resources/test_capture'


def alg2():
	print '1.1. Init Test Capture'
	
	cs = CaptureSource(trainingDataFile, headersFile)
	cs.initHeaders()
	cs.openCapture()
	global testCapture
	testCapture = cs.getTestCapture()
	cs.closeCapture()
	
	print '2.1. Convert To Points'
	
	global testPoints
	testPoints = {}
	global allPoints
	allPoints = []
	for k in list(testCapture.keys()):
		testPoints[k] = convertConnectionsToPoints(testCapture[k])
		allPoints.extend(testPoints[k])
	
	print '2.5. Calc Covariance'
	
#	Covariance.calcCovariance(allPoints)

	print '3.1. KMean Clustering'
	
	global kmean
	kmean = Kmean(testPoints, distanceFunc)
		
	print '4.1.  Test Clustering'
	testClusters(kmean)
	

def testClusters(kmean):

	print '4.1.1. Read Capture'

	resultFile = open('resources/results_new','w')
	cs = CaptureSource(testDataFile, headersFile)
	cs.initHeaders()
	cs.openCapture()
	realCapture = cs.getFullCapture()
	
	print '4.1.2. Convert to Points'

	points = convertConnectionsToPoints(realCapture)
	cs.closeCapture()
	ok = 0
	nok = 0
	size = len(points)
	for i in range(size):
		declaredCluster = str(realCapture[i].features['attack_type'].value)
		resultFile.write(declaredCluster)
		resultFile.write(' - ')
		#foundCluster = str(kmean.findClosestCluster(points[i]))
		foundCluster = str(kmean.findClosestByRadius(points[i]))
		resultFile.write(foundCluster + '\n')
		if foundCluster == declaredCluster:
			ok +=1
		else:
			nok +=1	
		print '{:.2%} - {:.3%}'.format(i/float(size), ok / float(i+1))
		
	resultFile.write('ok: ' + str(ok) +'\nnok: ' + str(nok))

def convertConnectionsToPoints(connections):	
	points = []
	for conn in connections:
		points.append(Point(conn))
	return points
	
def alg1():
		
	print '1.1. Begin read capture'
	connections = getCapture()
	print '1.2. End read capture'
	
	print '2.1. Begin convert to Points'
	points = []
	for conn in connections:
		points.append(Point(conn))
	print '2.2. End convert to points'
	
	print '3.1. Begin Clustering ' + str(len(points)) + ' points' 
	clusteringAlg = HierarchicalAlg(euclideanDistance)
	clusteringAlg.cluster(points)
	print '3.2. End Clustering'


if __name__ == '__main__':
	print '0. start'
	alg2()

