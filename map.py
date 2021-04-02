import location as loc
import prioqueue as pq

class Map(Graph):

	def __init__(this):
		super().__init__()

	def a_star_path(this,origin,target):
		queue = pq.PrioQueueMap()
		initial_element = pq.ElementQueueMap([origin],target)
		cur = queue.dequeue() #bentuknya list node
		while(cur[len(cur)-1].get_name() != target.get_name()):
			neighbor = cur[len(cur)-1].get_all_neighbor()
			new_track = cur
			for it in neighbor:
				new_track.append(it)
				queue.enqueue(new_track,target)
				new_track = cur
			cur = queue.dequeue()
		return cur