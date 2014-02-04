from ConnectionCapture import *
from DiscreteType import DiscreteType

def getCapture():
	captureSrcFile = open('resources/test_capture','r');
	captureMetaFile = open('resources/test_capture_head','r');
	headers = []
	connections = []
	for header in captureMetaFile:
		metric = header.split(':')
		if 'symbolic' in metric[1]:
			ConnectionCapture.captureHeaders[metric[0]] = DiscreteType()
		else:
			ConnectionCapture.captureHeaders[metric[0]] = float
		headers.append(metric[0])
	for capture in captureSrcFile:
		values = capture.split(',')
		connection = ConnectionCapture(headers, values)
		connections.append(connection)
	return connections

