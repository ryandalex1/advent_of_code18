data = [x for x in open("../input/day2_input.txt").readlines()]

for string in range(0, len(data)):
    for string_to_compare in data[0:string] + data[string:]:
        differences = 0
        for i in range(0, len(string_to_compare)):
            if differences > 1:
                break
            if string_to_compare[i] != data[string][i]:
                differences += 1
        if differences == 1:
            print(string)
            print(string_to_compare)