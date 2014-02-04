from DiscreteValue import DiscreteValue

class DiscreteType:
	def __init__(self):
		self.values = []
	def __call__(self, value):
		return DiscreteValue(value,self)		
	def toNum(self, value):
		if value not in self.values:
			self.values.append(value)
		return self.values.index(value)
