from graph import node_exception as ne

class Node:
	#ctor
	def __init__(this,value):
		this.name = value
		this.neighbor = []

	#exception null node
	def check_null_node(this):
		if (this.name == "NULL"):
			raise ne.NullNodeException("Violate a Null Node Value")
			##null node itu Node("NULL")

	#mendapatkan nama node
	def get_name(this):
		this.check_null_node()
		return this.name

	#mengganti nama node
	def set_name(this,new_name):
		this.check_null_node()
		this.name = new_name
		return

	#mendapatkan neighbor pada indeks tertentu
	def get_neighbor(this,neighbor_name):
		this.check_null_node()
		for it in this.neighbor:
			if (it.name == neighbor_name):
				return it
		return Node("NULL")

	#mendapatkan seluruh list neighbor
	def get_all_neighbor(this):
		return this.neighbor

	#mendapatkan panjang list neighbor
	def get_neighbor_num(this):
		this.check_null_node()
		return len(this.neighbor)

	#mengganti neighbor pada indeks tertentu di list neighbor
	def set_neighbor(this,i,value):
		this.check_null_node()
		if (i < len(this.neighbor)):
			neighbor_node = Node(value)
			this.neighbor[i] = neighbor_node
			return True
		return False

	#menambah neighbor
	def add_neighbor(this,neighbor_node):
		this.check_null_node()
		this.neighbor.append(neighbor_node)
		return

	#menghapus neighbor dengan nama tertentu
	def del_neighbor(this,neighbor_name):
		this.check_null_node()
		i = 0
		neighbor_node = Node("NULL")
		found = False
		while(i < len(this.neighbor) and not(found)):
			if (this.neighbor[i].name != neighbor_name):
				i += 1
			else:
				neighbor_node = this.neighbor[i]
				this.neighbor.remove(neighbor_node)
				found = True
		return neighbor_node

	#mengecek keberadaan neighbor
	def is_exist_neighbor(this,neighbor_name):
		for it in this.neighbor:
			if (it.name == neighbor_name):
				return True
		return False

	#mengecek null node
	def is_null(this):
		return this.name == "NULL"

	#untuk debugging
	def print_all(this):
		this.check_null_node()
		print("Node name: " + this.name)
		print("Neighbor(s) : ")
		for i in range(len(this.neighbor)):
			print("- " + this.neighbor[i].name)
		return