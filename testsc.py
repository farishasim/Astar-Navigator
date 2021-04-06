import folium
import map
import location as loc
import mapLoader as ml
import mapVisualizer as mv
import os
import webbrowser



peta = ml.MapLoader().load("test/testITB2.txt")
# peta.print_all()
node1 = input()
node2 = input()

# result = peta.a_star_path(a,h)
result = peta.a_star_path2(peta.get_node(node1),peta.get_node(node2))
# print(result)
if (len(result[0]) != 0):
    for i in result[0]:
        print(i.get_name())
    print("%.2f" % result[1])
    mv.MapVisualizer().visualize(peta, result[0])
    url = 'file:///' + os.getcwd() + '/' + 'testscmap.html'
    webbrowser.open(url) 
    
else:
    print("not connected")