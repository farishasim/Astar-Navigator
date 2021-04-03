import map
import location as loc

jakarta = loc.Location("Jakarta",0,0)
surabaya = loc.Location("Surabaya",20,6)
makassar = loc.Location("Makassar",20,15)

peta = map.Map()
peta.add_node(jakarta)
peta.add_node(surabaya)

peta.print_all()