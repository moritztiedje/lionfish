landSize = 4

area_map = []

coastline = []
for _ in range(landSize + 2):
    coastline.append(0)

area_map.append(coastline)

landline = []
landline.append(0)
for _ in range(landSize):
    landline.append(1)
landline.append(0)

for _ in range(landSize):
    area_map.append(landline)

area_map.append(coastline)

dummyMapFile = open("./dummyMap", mode="wb")
for line in area_map:
    dummyMapFile.write(bytearray(line))
    dummyMapFile.write(b'\x02')
