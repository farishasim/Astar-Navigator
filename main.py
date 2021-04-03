import map
import location as loc
import mapLoader as ml

# a = loc.Location("A",1.1818181818182,5.9145454545455)
# b = loc.Location("B",3.6818181818182,5.5945454545455)
# c = loc.Location("C",2.1618181818182,4.3145454545455)
# d = loc.Location("D",0.6818181818182,3.4945454545455)
# e = loc.Location("E",5.1418181818182,4.1745454545455)
# f = loc.Location("F",3.7818181818182,2.7745454545455)
# g = loc.Location("G",1.2818181818182,1.5745454545455)
# h = loc.Location("H",6.1618181818182,2.7945454545455)

# peta = map.Map()
# peta.add_node(a)
# peta.add_node(b)
# peta.add_node(c)
# peta.add_node(d)
# peta.add_node(e)
# peta.add_node(f)
# peta.add_node(g)
# peta.add_node(h)

# #tetangga a
# tetangga_a = ["B","C","D"]
# tetangga_b = ["A","C","E","F"]
# tetangga_c = ["A","B","F","G"]
# tetangga_d = ["A","F","G"]
# tetangga_e = ["B","F","H"]
# tetangga_f = ["B","C","D","E"]
# tetangga_g = ["C","D"]
# tetangga_h = ["E","F"]

# peta.add_many_edge("A",tetangga_a)
# peta.add_many_edge("B",tetangga_b)
# peta.add_many_edge("C",tetangga_c)
# peta.add_many_edge("D",tetangga_d)
# peta.add_many_edge("E",tetangga_e)
# peta.add_many_edge("F",tetangga_f)
# peta.add_many_edge("G",tetangga_g)
# peta.add_many_edge("H",tetangga_h)

peta = ml.MapLoader().load("test/testfile.txt")

# peta.print_all()

# result = peta.a_star_path(a,h)
result = peta.a_star_path(peta.get_node("A"),peta.get_node("H"))
print(result)
for i in result:
    print(i.get_name())