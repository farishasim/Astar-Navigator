class ElementQueueMap:
	def __init__(this,track,target):
		this.track = track
		this.prio = 0

		length = len(this.track)
		if (length > 0):
			i = 0
			while(i+1 < length)
				temp_dist = this.track[i].distance(this.track[i+1])
				this.prio += temp_dist
				i += 1
			this.prio += this.track[length-1].distance(target)

	def prio(this):
		return this.prio

	def track(this):
		return this.track

class PrioQueueMap:
	def __init__(this):
		this.queue = []

	def sort_queue(this):
		length = len(this.queue)
		for i in range(length):
			for j in range(i+1,length):
				if (this.queue[j].prio() < this.queue[i].prio()):
					temp = this.queue[i]
					this.queue[i] = this.queue[j]
					this.queue[j] = temp

	def enqueue(this,element):
		this.queue.append(element)
		this.sort_queue()

	def dequeue(this):
		if (len(this.queue) > 0):
			result = this.queue.pop(0)
			return result
		return None

	def get_size(this):
		return len(this.queue)