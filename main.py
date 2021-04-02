from graph import node
from graph import graph
import coordinate2d as c2d
#main
# first_obj = node.Node("Laos")
# first_obj.add_neighbor("Indonesia")
# first_obj.add_neighbor("Argentina")

# first_obj.print_all()
# point_one = c2d.Coordinate2D(10,3)
# point_two = c2d.Coordinate2D(-1,200)

# print(point_one.euclidean_distance(point_two))

nodea = node.Node("A")
nodeb = node.Node("B")
nodec = node.Node("C")
noded = node.Node("D")
nodee = node.Node("E")
nodef = node.Node("F")
nodeg = node.Node("G")
nodeh = node.Node("H")

graf = graph.Graph()
graf.add_node(nodea)
graf.add_node(nodeb)
graf.add_node(nodec)
graf.add_node(noded)
graf.add_node(nodee)
graf.add_node(nodef)
graf.add_node(nodeg)
graf.add_node(nodeh)

graf.add_edge("A","B")
graf.add_edge("A","C")
graf.add_edge("A","D")

graf.add_edge("B","E")
graf.add_edge("B","F")
graf.add_edge("B","C")

graf.add_edge("C","F")
graf.add_edge("C","G")

graf.add_edge("D","G")
graf.add_edge("D","F")

graf.add_edge("E","F")
graf.add_edge("E","H")

graf.add_edge("F","H")

graf.add_edge("B","A")

# graf.del_node("A")
# graf.del_node("B")
# graf.del_node("C")
# graf.del_node("Z")

#my_node = graf.get_node("A").get_neighbor("C")

graf.print_all()

#my_node.print_all()