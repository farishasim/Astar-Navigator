import map
import folium

class MapVisualizer:
    def visualize(self, mapSolved, path, distance):
        self.visualMap = folium.Map(location=[mapSolved.nodes[0].coordinate.x, 
                                        mapSolved.nodes[0].coordinate.y], 
                                zoom_start=17)

        # create marker for each node
        self.visualizeMap(mapSolved)

        # create marker for each node in path
        self.visualizePath(path, distance)

        print("You can see the result in : " + "testscmap.html")
        self.visualMap.save('testscmap.html')


    
    def visualizeMap(self, mapSolved):
        for node in mapSolved.nodes:
            folium.Marker([node.coordinate.x, 
                            node.coordinate.y],
                            popup='<strong>'+node.get_name()+'</strong>',
                            icon=folium.Icon(icon='leaf', color='blue')).add_to(self.visualMap)
        
        for node1 in mapSolved.nodes:
            for node2 in mapSolved.nodes:
                if mapSolved.is_exist_edge(node1.get_name(), node2.get_name()):
                    folium.PolyLine([[node1.coordinate.x, node1.coordinate.y],
                                    [node2.coordinate.x, node2.coordinate.y]],
                                    color='blue').add_to(self.visualMap)

    def visualizePath(self, path, distance):
        countNodes = len(path)
        points = []
        for i in range(countNodes):
            node = path[i]
            points.append([node.coordinate.x, node.coordinate.y])
        
        folium.PolyLine(points,
                        color='red',
                        popup='<strong>'+"%.2f" % distance + " metres"+'</strong>',
                        tooltip=("%.2f" % distance + " metres")).add_to(self.visualMap)