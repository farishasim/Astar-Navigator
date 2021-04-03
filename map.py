import location as loc
import prioqueue as pq
from graph import graph
from graph import node

class Map(graph.Graph):

	def __init__(this):
		super().__init__()

	def a_star_path(this,origin,target):
		queue = pq.PrioQueueMap()
		initial_element = pq.ElementQueueMap([origin],target)
		queue.enqueue(initial_element)
		cur = queue.dequeue().track #bentuknya list node
		while(cur[len(cur)-1].get_name() != target.get_name() and queue.flag):
			neighbor = cur[len(cur)-1].get_all_neighbor()
			new_track = cur[:]
			i = 0
			for it in neighbor:
				new_track.append(it)
				new_elqueue = pq.ElementQueueMap(new_track,target)
				queue.enqueue(new_elqueue)
				new_track = cur[:]
			cur = queue.dequeue().track
		if (not(queue.flag)):
			return None
		return cur