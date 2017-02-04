landSize = 4

map = []

coastline = []
for _ in range(landSize + 2):
    coastline.append(0)

map.append(coastline)

landline = []
landline.append(0)
for _ in range(landSize):
    landline.append(1)
landline.append(0)

for _ in range(landSize):
    map.append(landline)

map.append(coastline)

dummyMapFile = open("./dummyMap", mode="wb")
for line in map:
    dummyMapFile.write(bytearray(line))
    dummyMapFile.write(b'\x02')