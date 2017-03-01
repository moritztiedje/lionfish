from random import randint

map_size = 100
number_of_sparks = 40

world_map = []
for _ in range(100):
    world_map.append([None] * map_size)

sparks = []
for i in range(0, number_of_sparks):
    random_spark = randint(0, map_size * map_size - 1)
    sparks.append((random_spark % map_size, int(random_spark / map_size)))

land = 1
water = 0

growth_cells = []

for spark in sparks:
    if world_map[spark[0]][spark[1]] is None:
        world_map[spark[0]][spark[1]] = land
        growth_cells.append(spark)


def random_next_land_cell():
    if randint(0, 100) > 70:
        return water
    else:
        return land


def grow_top_water_tile():
    if growth_cell[0] is not 0:
        adjacent = (growth_cell[0] - 1, growth_cell[1])
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = water
            growth_cells.append(adjacent)


def grow_bottom_water_tile():
    if growth_cell[0] is not map_size - 1:
        adjacent = (growth_cell[0] + 1, growth_cell[1])
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = water
            growth_cells.append(adjacent)


def grow_left_water_tile():
    if growth_cell[1] is not 0:
        adjacent = (growth_cell[0], growth_cell[1] - 1)
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = water
            growth_cells.append(adjacent)


def grow_right_water_tile():
    if growth_cell[1] is not map_size - 1:
        adjacent = (growth_cell[0], growth_cell[1] + 1)
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = water
            growth_cells.append(adjacent)


def grow_top_land_tile():
    if growth_cell[0] is not 0:
        adjacent = (growth_cell[0] - 1, growth_cell[1])
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = random_next_land_cell()
            growth_cells.append(adjacent)


def grow_bottom_land_tile():
    if growth_cell[0] is not map_size - 1:
        adjacent = (growth_cell[0] + 1, growth_cell[1])
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = random_next_land_cell()
            growth_cells.append(adjacent)


def grow_left_land_tile():
    if growth_cell[1] is not 0:
        adjacent = (growth_cell[0], growth_cell[1] - 1)
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = random_next_land_cell()
            growth_cells.append(adjacent)


def grow_right_land_tile():
    if growth_cell[1] is not map_size - 1:
        adjacent = (growth_cell[0], growth_cell[1] + 1)
        if world_map[adjacent[0]][adjacent[1]] is None:
            world_map[adjacent[0]][adjacent[1]] = random_next_land_cell()
            growth_cells.append(adjacent)


while len(growth_cells) is not 0:
    growth_cell = growth_cells[0]
    del growth_cells[0]

    if world_map[growth_cell[0]][growth_cell[1]] is water:
        grow_top_water_tile()
        grow_bottom_water_tile()
        grow_left_water_tile()
        grow_right_water_tile()

    if world_map[growth_cell[0]][growth_cell[1]] is land:
        grow_top_land_tile()
        grow_bottom_land_tile()
        grow_left_land_tile()
        grow_right_land_tile()

generatedMapFile = open("./dummyWorldMap", mode="wb")
for line in world_map:
    generatedMapFile.write(bytearray(line))
    generatedMapFile.write(b'\x02')
