import folium
import map
import location as loc
import mapLoader as ml
import mapVisualizer as mv
import os
import webbrowser

filename = input("Masukkan nama file txt : ")

peta = ml.MapLoader().load("../test/" + filename)

print("Simpul-simpul yang tersedia : ")
for node in peta.nodes:
    print(node.get_name(), end=" ")
print()

node1 = input("Masukkan simpul awal : ")
node2 = input("Masukkan simpul tujuan : ")

result = peta.a_star_path2(peta.get_node(node1),peta.get_node(node2))

if (len(result[0]) != 0):
    for i in range(len(result[0])):
        print(result[0][i].get_name() , end = "")
        if (i != len(result[0]) -1):
            print(" --> " , end = "")
        else:
            print()
    # for i in result[0]:
    #     print(i.get_name() , end = "")
    print("%.2f" % result[1] + " metres")
    mv.MapVisualizer().visualize(peta, result[0], result[1])
    url = 'file:///' + os.getcwd() + '/' + 'testscmap.html'
    webbrowser.open(url) 
    
else:
    print("not connected")