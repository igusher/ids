class DiscreteValue:
	def __init__(self, val, metricType):
		self.value = val
		self.metricType = metricType
	def __abs__(self):
		return self.metricType.toNum(self.value)
