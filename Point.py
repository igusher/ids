from capturemodel.ConnectionCapture import *
class Point:
	def __init__(self, connCapture):
		self.vector = []
		keys = list(connCapture.features.keys())
		for key in keys:
			if "attack_type" in key:
				continue;
			self.vector.append(connCapture.features[key].__abs__())
		self.id = connCapture.id

	def getId(self):
		return self.id
	

			
