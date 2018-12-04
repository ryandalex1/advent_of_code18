data = [x for x in open("../input/day3_input.txt").readlines()]

claims = set()
total_overlap = 0

for line in data:
    inches_from_left = int(line[line.find("@") + 1: line.find(",")].strip())
    inches_from_top = int(line[line.find(",") + 1: line.find(":")].strip())
    width = int(line[line.find(":") + 1: line.find("x")].strip())
    height = int(line[line.find("x") + 1:].strip())

    for x_value in range(inches_from_left, inches_from_left + width):
        for y_value in range(inches_from_top, inches_from_top + height):
            if (x_value, y_value, 0) in claims:
                total_overlap += 1
                claims.remove((x_value, y_value, 0))
                claims.add((x_value, y_value, 1))

            elif (x_value, y_value, 1) in claims:
                pass

            else:
                claims.add((x_value, y_value, 0))

print(total_overlap)