from ast import literal_eval as make_tuple
points = open("../input/day6_input.txt").readlines()


def find_total_distance(point):
    total = 0
    for coords in point_tuples:
        total += abs(point[0] - coords[0]) + abs(point[1] - coords[1])
    return total


point_tuples = []
for given_point in points:
    point_tuples.append(make_tuple(given_point.strip()))

grid_array = []
for x in range(500):
    for y in range(500):
        grid_array.append((x, y))

region_size = 0
for grid_point in grid_array:
    if find_total_distance(grid_point) < 10000:
        region_size += 1

print(region_size)