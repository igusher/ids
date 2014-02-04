from capturemodel.CaptureSource import *
from Point import Point

if __name__ == '__main__':
	connections = getCapture()
	points = []
	for conn in connections:
		points.append(Point(conn))
