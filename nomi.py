from geopy.geocoders import Nominatim

nom = Nominatim(user_agent='tutorial')

#print(nom.latitude)

while True:
    place = input()
    n = nom.geocode(place)
    print(n.address)
    print("Koordinat", place, ": (", n.latitude, ",", n.longitude, ")")
    #dir(n)
