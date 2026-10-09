north = {"New York", "Dallas", "Miami"}
south = {"Miami", "Atlanta", "Dallas"}

print("North Region:", north)
print("South Region:", south)

#union:all unique delivering cities
all_cities = north.union(south)

print("\nAll Delivering Cities:", all_cities)

#intersection: cities served by both regions
common_cities = north.intersection(south)
print("Common Cities:", common_cities)

#difference: cities unique to one region
north_only = north.difference(south)

print("North Only:", north_only)

