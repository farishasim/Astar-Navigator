import map
import location as loc

class MapLoader:
    def __init__(self):
        # test
        self.test = True

    def load(self, filename):
        mapLoaded = map.Map()
        f = open(filename, 'r')

        countNodes = int(f.readline())
        nodes = ["X" for i in range(countNodes)]

        # read location/node
        for i in range(countNodes):
            lines = f.readline().split(' ')
            nodes[i] = lines[0]
            mapLoaded.add_node(loc.Location(lines[0], float(lines[1]), float(lines[2])))

        # read edge
        for i in range(countNodes):
            lines = f.readline().split(' ')
            this_name = nodes[i]
            for j in range(countNodes):
                other_name = nodes[j]
                if lines[j] == "1":
                    mapLoaded.add_edge(this_name, other_name)

        return mapLoaded