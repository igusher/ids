from ConnectionCapture import *
from DiscreteType import DiscreteType

class CaptureSource:
	def __init__(self, captureFileName, headersFileName):
		self.captureFileName = captureFileName
		self.headersFileName = headersFileName
		self.id = 0
	def initHeaders(self):
		self.headers = []
		headerFile = open(self.headersFileName)
		for header in headerFile:
			metric = header.split(':')
			if 'symbolic' in metric[1]:
				ConnectionCapture.captureHeaders[metric[0]] = DiscreteType()
			else:
				ConnectionCapture.captureHeaders[metric[0]] = float
			self.headers.append(metric[0])
		headerFile.close()

	def openCapture(self):
		self.captureFile = open(self.captureFileName)

	def getFullCapture(self):
		connections = []
		for capture in self.captureFile:
			connection = ConnectionCapture.fromCaptureStr(self.headers,capture, self.id)
			connections.append(connection)
			self.id += 1
		return connections
	
	def getNextCapture(self):
		connection = ConnectionCapture.fromCaptureStr(self.headers, self.captureFile.readline(), self.id)
		self.id += 1
		return connection

	def getTestCapture(self):
		testCapture = {}
		for capture in self.captureFile:
			connection = ConnectionCapture.fromCaptureStr(self.headers, capture, self.id)
			atckType = connection.features['attack_type'].value
			if atckType not in testCapture:
				testCapture[atckType] = []
			testCapture[atckType].append(connection)
			self.id += 1
		return testCapture
	
	def closeCapture(self):
		self.captureFile.close()

