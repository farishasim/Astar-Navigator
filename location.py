from graph import node
import coordinate2d as c2d

#derived class of Node
class Location(node.Node):
	#ctor
	def __init__(this,name,x,y):
		super().__init__(name)
		this.coordinate = c2d.Coordinate2D(x,y)
	#memperoleh jarak antara dua buah lokasi
	def distance(this,another_location):
		return this.coordinate.haversine_distance(another_location.coordinate)