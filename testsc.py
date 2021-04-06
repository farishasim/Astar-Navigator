import folium
import map
import location as loc
import mapLoader as ml
import mapVisualizer as mv
import os
import webbrowser
from geojson import Feature, FeatureCollection, Polygon, dump


peta = ml.MapLoader().load("test/testITB2.txt")
# peta.print_all()
node1 = input()
node2 = input()

# result = peta.a_star_path(a,h)
result = peta.a_star_path2(peta.get_node(node1),peta.get_node(node2))
# print(result)
if (len(result) != 0):
    for i in result:
        print(i.get_name())
    mv.MapVisualizer().visualize(peta, result)
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