from capturemodel.CaptureSource import *
from Point import Point
from mymath.distance import *
from mymath.hierarchical import *
from mymath.kmean import *



def alg2():
	print '1.1. Init Test Capture'
	cs = CaptureSource('resources/test_capture_back', 'resources/test_capture_head')
	cs.initHeaders()
	cs.openCapture()
	global testCapture
	testCapture = cs.getTestCapture()
	cs.closeCapture()
	print '2.1. Convert To Points'
	global testPoints
	testPoints = {}
	for k in list(testCapture.keys()):
		testPoints[k] = []
		for conn in testCapture[k]:
			testPoints[k].append(Point(conn))
	print '3.1. KMean Clustering'
	global kmean 
	kmean = Kmean(testPoints, euclideanDistance)
	print '4.1. Test Clustering'
	
	resultFile = open('resources/results','w')
	cs = CaptureSource('resources/test_capture_back', 'resources/test_capture_head')
	cs.initHeaders()
	cs.openCapture()
	realCapture = cs.getFullCapture()
	
	points = []
	for conn in realCapture:
		points.append(Point(conn))
	cs.closeCapture()
	ok = 0
	nok = 0
	for i in range(len(points)):
		declaredCluster = str(realCapture[i].features['attack_type'].value)
		resultFile.write(declaredCluster)
		resultFile.write(' - ')
		foundCluster = str(kmean.findClosestCluster(points[i]))
		resultFile.write(foundCluster + '\n')
		if foundCluster == declaredCluster:
			ok +=1
		else:
			nok +=1
		
	resultFile.write('ok: ' + str(ok) +'\nnok: ' + str(nok))

if __name__ == '__main__':
	print '0. start'
	alg2()

	
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

