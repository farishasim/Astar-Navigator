from graph import node

class Graph:
	def __init__(this):
		this.nodes = []

	def add_node(this,node): ##typenya Node atau subclassnya aja
		this.nodes.append(node)
		return

	def get_node_idx(this,node_name):
		for i in range(len(this.nodes)):
			if (this.nodes[i].get_name() == node_name):
				return i
		return -1

	def get_node(this,node_name):
		idx = this.get_node_idx(node_name)
		if (idx != -1):
			return this.nodes[idx]
		return Node("NULL")

	def is_exist_edge(this,node1_name,node2_name):
		first = this.get_node(node1_name).is_exist_neighbor(node2_name)
		second = this.get_node(node2_name).is_exist_neighbor(node1_name)
		return first or second

	def add_edge(this,node1_name,node2_name):
		node1_idx = this.get_node_idx(node1_name)
		node2_idx = this.get_node_idx(node2_name)
		if (node1_idx != -1 and node2_idx != -1):
			if (not(this.is_exist_edge(node1_name,node2_name))):
				this.nodes[node1_idx].add_neighbor(this.nodes[node2_idx])
				this.nodes[node2_idx].add_neighbor(this.nodes[node1_idx])
				return True
		return False

	def del_edge(this,node1_name,node2_name):
		node1_idx = this.get_node_idx(node1_name)
		node2_idx = this.get_node_idx(node2_name)
		if (node1_idx != -1 and node2_idx != -1):
			if(this.is_exist_edge(node1_name,node2_name)):
				this.nodes[node1_idx].del_neighbor(node2_name)
				this.nodes[node2_idx].del_neighbor(node1_name)
				return True
		return False


	def del_node(this,node_name):
		for i in range(len(this.nodes)):
			this.nodes[i].del_neighbor(node_name)
		idx = this.get_node_idx(node_name)
		if (idx != -1):
			value = this.nodes[idx]
			this.nodes.remove(this.nodes[idx])
			return value
		return node.Node("NULL")


	def print_all(this):
		for it in this.nodes:
			it.print_all()