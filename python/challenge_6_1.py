from ast import literal_eval as make_tuple
points = open("../input/day6_input.txt").readlines()
point_tuples = set()
point_area_dict = {}
for point in points:
    point_tuples.add(make_tuple(point.strip()))
    point_area_dict[make_tuple(point.strip())] = 0


def find_distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


points_on_graph = {}
for x in range(600):
    points_on_graph[x] = []
    for y in range(600):
        points_on_graph[x].append({y: []})

for point in point_tuples:
    for x in range(600):
        for y in range(600):
            if not points_on_graph[x][y][y]:
                points_on_graph[x][y][y] = []
                points_on_graph[x][y][y].append(point)
                points_on_graph[x][y][y].append(find_distance(point, (x, y)))
                point_area_dict[point] += 1

            else:
                if find_distance(point, (x, y)) < points_on_graph[x][y][y][1]:
                    point_area_dict[point] += 1
                    try:
                        point_area_dict[points_on_graph[x][y][y][0]] -= 1
                    except KeyError:
                        pass
                    points_on_graph[x][y][y] = []
                    points_on_graph[x][y][y].append(point)
                    points_on_graph[x][y][y].append(find_distance(point, (x, y)))

                elif find_distance(point, (x, y)) == points_on_graph[x][y][y][1]:
                    try:
                        point_area_dict[points_on_graph[x][y][y][0]] -= 1
                    except KeyError:
                        pass
                    points_on_graph[x][y][y] = []
                    points_on_graph[x][y][y].append(None)
                    points_on_graph[x][y][y].append(find_distance(point, (x, y)))

                else:
                    pass


def find_if_higher_value(value, values_to_compare):
    if value < max(values_to_compare):
        return True
    return False


def find_if_lower_value(value, values_to_compare):
    if value > min(values_to_compare):
        return True
    return False


not_infinite = set()

# for x in range(0, 999):
#     print(points_on_graph[0][x][x][0])

for point in point_tuples:
    if(point not in [points_on_graph[0][x_val][x_val][0] for x_val in range(0, 600)] and
       point not in [points_on_graph[599][x_val][x_val][0] for x_val in range(0, 600)] and
       point not in [points_on_graph[x_val][0][0][0] for x_val in range(0, 600)] and
       point not in [points_on_graph[599][0][0][0] for x_val in range(0, 600)]):
            not_infinite.add(point)


for x in sorted(not_infinite):
    print(x)

print(sorted([point_area_dict[point] for point in not_infinite]))
print(max([point_area_dict[point] for point in not_infinite]))