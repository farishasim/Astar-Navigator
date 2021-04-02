from graph import node
import coordinate2d as c2d

class Location(Node):
	def __init__(this,name,x,y):
		super().__init__(name)
		this.coordinate = c2d.Coordinate2D(x,y)

	def distance(this,another_location):
		return this.coordinate.euclidean_distance(another_location.coordinate)