import math

class Coordinate2D:
	def __init__(this,x,y):
		this.x = x
		this.y = y

	def euclidean_distance(this,another_point):
		lat1 = math.radians(this.x)
		lat2 = math.radians(another_point.x)
		lon1 = math.radians(this.y)
		lon2 = math.radians(another_point.y)

		#Haversine
		delta_lat = lat2 - lat1
		delta_lon = lon2 - lon1
		a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon/2)**2
		c = 2 * math.asin(math.sqrt(a))
		earth_r = 6371
		return (c * earth_r * 1000)