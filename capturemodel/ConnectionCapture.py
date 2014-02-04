from DiscreteValue import DiscreteValue

class ConnectionCapture:
	captureHeaders = {}
	def __init__(self, metrics, values):
		self.features = {}
		if len(metrics) != len(values):
			raise ValueError("'metrics' object and 'values' have different size")
		for i in range(len(metrics)):
			values[i] = values[i].strip()
			self.features[metrics[i]] =  ConnectionCapture.captureHeaders[metrics[i]](values[i])
