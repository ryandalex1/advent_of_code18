data = [x for x in open("../input/day2_input.txt").readlines()]

threes = 0
twos = 0

for string in data:
    letter_values = {}
    for letter in string:
        if letter in letter_values:
            letter_values[letter] = letter_values[letter] + 1
        else:
            letter_values[letter] = 1
    if 2 in letter_values.values():
        twos += 1
    if 3 in letter_values.values():
        threes += 1

print("Threes -> " + str(threes) + "\n")
print("Twos -> " + str(twos) + "\n")
print("Checksum -> " + str(twos*threes))