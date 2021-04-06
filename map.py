import location as loc
import prioqueue as pq
from graph import graph
from graph import node

class Map(graph.Graph):

	def __init__(this):
		super().__init__()

	def a_star_path(this,origin,target):
		if (origin.is_null() or target.is_null()):
			return ([],-1)
		if (this.dfs_search(origin.get_name(),target.get_name())):
			queue = pq.PrioQueueMap()
			initial_element = pq.ElementQueueMap([origin],target)
			queue.enqueue(initial_element)
			firstdeq = queue.dequeue()
			cur = firstdeq.track #bentuknya list node
			distance = firstdeq.prio
			while(cur[len(cur)-1].get_name() != target.get_name() and queue.flag):
				neighbor = cur[len(cur)-1].get_all_neighbor()
				new_track = cur[:]
				i = 0
				for it in neighbor:
					new_track.append(it)
					new_elqueue = pq.ElementQueueMap(new_track,target)
					queue.enqueue(new_elqueue)
					new_track = cur[:]
				new_dequeue = queue.dequeue()
				cur = new_dequeue.track
				distance = new_dequeue.prio
			if (not(queue.flag)):
				return ([],-1)
			return (cur,distance)
		return ([],-1)

	# alternatif lain tanpa dfs
	def a_star_path2(this,origin,target):
		# if (this.dfs_search(origin.get_name(),target.get_name())):
		if (origin.is_null() or target.is_null()):
			return ([],-1)
		visited_dict = {}
		for nodes in this.nodes:
			visited_dict[nodes.get_name()] = False
		queue = pq.PrioQueueMap()
		initial_element = pq.ElementQueueMap([origin],target)
		queue.enqueue(initial_element)
		cur = initial_element.track
		distance = initial_element.prio
		while(cur[len(cur)-1].get_name() != target.get_name() and len(queue.queue) != 0):
			new_dequeue = queue.dequeue()
			cur = new_dequeue.track #bentuknya list node
			distance = new_dequeue.prio
			visited_dict.update({cur[len(cur)-1].get_name() : True}) # tandai sudah dikunjungi
			neighbor = cur[len(cur)-1].get_all_neighbor()
			new_track = cur[:]
			for it in neighbor:
				if not visited_dict.get(it.get_name()):
					new_track.append(it)
					new_elqueue = pq.ElementQueueMap(new_track,target)
					queue.enqueue(new_elqueue)
					new_track = cur[:]
		if (len(queue.queue) == 0):
			return ([],-1)
		return (cur,distance)
		# return []