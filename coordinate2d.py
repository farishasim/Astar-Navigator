import math

class Coordinate2D:
	def __init__(this,x,y):
		this.x = x
		this.y = y

	def euclidean_distance(this,another_point):
		delta_x = this.x - another_point.x
		delta_y = this.y - another_point.y
		return math.sqrt(delta_x**2 + delta_y**2)