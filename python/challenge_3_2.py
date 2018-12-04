data = [x for x in open("../input/day3_input.txt").readlines()]

claims = set()
pieces_in_a_claim = {}
overlap_per_piece = {}

for line in data:
    line_number = int(line[line.find("#") + 1: line.find("@")].strip())
    inches_from_left = int(line[line.find("@") + 1: line.find(",")].strip())
    inches_from_top = int(line[line.find(",") + 1: line.find(":")].strip())
    width = int(line[line.find(":") + 1: line.find("x")].strip())
    height = int(line[line.find("x") + 1:].strip())

    overlap_per_piece[line_number] = 0

    for x_value in range(inches_from_left, inches_from_left + width):
        for y_value in range(inches_from_top, inches_from_top + height):

            # Point seen once
            if (x_value, y_value, 0) in claims:
                claims.remove((x_value, y_value, 0))
                claims.add((x_value, y_value, 1))
                pieces_in_a_claim[(x_value, y_value)].append(line_number)
                for piece in pieces_in_a_claim[(x_value, y_value)]:
                    overlap_per_piece[piece] += 1

            # Point seen before more than once
            elif (x_value, y_value, 1) in claims:
                pieces_in_a_claim[(x_value, y_value)].append(line_number)
                for piece in pieces_in_a_claim[(x_value, y_value)]:
                    overlap_per_piece[piece] += 1

            # Point never seen before
            else:
                claims.add((x_value, y_value, 0))
                pieces_in_a_claim[(x_value, y_value)] = [line_number]

for key in overlap_per_piece:
    if overlap_per_piece[key] == 0:
        print(key)

