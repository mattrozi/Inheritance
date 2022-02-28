import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


# This will not work, it only works for flowers.
# print(primrose.get_petals())
