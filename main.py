import folium
import map
import location as loc
import mapLoader as ml
import mapVisualizer as mv
import os
import webbrowser



peta = ml.MapLoader().load("test/testITB2.txt")

node1 = input()
node2 = input()

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
    mv.MapVisualizer().visualize(peta, result[0])
    url = 'file:///' + os.getcwd() + '/' + 'testscmap.html'
    webbrowser.open(url) 

        # polygon = []
    # for node in result:
    #     polygon.append((node.coordinate.x, node.coordinate.y))

    # features = []
    # poly1 = Polygon([polygon])

    # features.append(Feature(geometry=poly1))

    # feature_collection = FeatureCollection(features)

    # with open('result.geojson', 'w') as f:
    #     dump(feature_collection, f, indent=2)
    # f.close()
    
else:
    print("not connected")