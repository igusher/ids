from capturemodel.ConnectionCapture import *
class Point:
	def __init__(self, connCapture):
		self.vector = []
		keys = list(connCapture.features.keys())
		for key in keys:
			self.vector.append(connCapture.features[key].__abs__())
	
	

			
