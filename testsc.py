import folium
import map
import location as loc
import mapLoader as ml
import mapVisualizer as mv



peta = ml.MapLoader().load("test/testITB2.txt")
# peta.print_all()

# result = peta.a_star_path(a,h)
result = peta.a_star_path2(peta.get_node("A"),peta.get_node("H"))
# print(result)
if (len(result) != 0):
    for i in result:
        print(i.get_name())
    mv.MapVisualizer().visualize(peta, result)    
    
else:
    print("not connected")