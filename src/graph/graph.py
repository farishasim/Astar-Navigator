from graph import node

class Graph:
	#ctor
	def __init__(this):
		this.nodes = []

	#menambah node
	def add_node(this,node): ##typenya Node atau subclassnya aja
		this.nodes.append(node)
		return

	#mendapatkan indeks tertentu sebuah node dengan param nama
	def get_node_idx(this,node_name):
		for i in range(len(this.nodes)):
			if (this.nodes[i].get_name() == node_name):
				return i
		return -1

	#mendapatkan return value dengan tipe kelas Node menggunakan param nama
	def get_node(this,node_name):
		idx = this.get_node_idx(node_name)
		if (idx != -1):
			return this.nodes[idx]
		return node.Node("NULL")

	#mengcek apakah dua node dengan nama tertentu bersisian
	def is_exist_edge(this,node1_name,node2_name):
		first = this.get_node(node1_name).is_exist_neighbor(node2_name)
		second = this.get_node(node2_name).is_exist_neighbor(node1_name)
		return first or second

	#menambah sisi
	def add_edge(this,node1_name,node2_name):
		node1_idx = this.get_node_idx(node1_name)
		node2_idx = this.get_node_idx(node2_name)
		if (node1_idx != -1 and node2_idx != -1):
			if (not(this.is_exist_edge(node1_name,node2_name))):
				this.nodes[node1_idx].add_neighbor(this.nodes[node2_idx])
				this.nodes[node2_idx].add_neighbor(this.nodes[node1_idx])
				return True
		return False

	#menambah sisi banyak sekaligus
	def add_many_edge(this,node_name,list_node_name):
		for i in list_node_name:
			this.add_edge(node_name,i)

	#menghilangkan sebuah sisi
	def del_edge(this,node1_name,node2_name):
		node1_idx = this.get_node_idx(node1_name)
		node2_idx = this.get_node_idx(node2_name)
		if (node1_idx != -1 and node2_idx != -1):
			if(this.is_exist_edge(node1_name,node2_name)):
				this.nodes[node1_idx].del_neighbor(node2_name)
				this.nodes[node2_idx].del_neighbor(node1_name)
				return True
		return False

	#menghilangkan sebuah node
	def del_node(this,node_name):
		for i in range(len(this.nodes)):
			this.nodes[i].del_neighbor(node_name)
		idx = this.get_node_idx(node_name)
		if (idx != -1):
			value = this.nodes[idx]
			this.nodes.remove(this.nodes[idx])
			return value
		return node.Node("NULL")

	#untuk mencari keterhubungan dua buah node
	def dfs_search(this,node1_name,node2_name):
		node1_idx = this.get_node_idx(node1_name)
		if (node1_idx == -1 or this.get_node_idx(node2_name) == -1):
			return False
		visited = [0 for i in range(len(this.nodes))]
		visited[node1_idx] = 1
		record = [node1_name]
		while(node1_name != node2_name):
			node1 = this.get_node(node1_name)
			list_neighbor = node1.get_all_neighbor()
			found = False
			i = 0
			while(i < len(list_neighbor) and not found):
				neighbor_name = list_neighbor[i].get_name()
				neighbor_idx = this.get_node_idx(neighbor_name)
				if (visited[neighbor_idx] == 0):
					visited[neighbor_idx] = 1
					record.append(neighbor_name)
					node1_name = neighbor_name
					found = True
				else:
					i += 1
			if (node1_name == node2_name):
				return True
			if (i == len(list_neighbor)):
				length = len(record)
				if (length == 1):
					return False
				else:
					record.pop(length-1)
					node1_name = record[length-2]

	#untuk debugging
	def print_all(this):
		for it in this.nodes:
			it.print_all()