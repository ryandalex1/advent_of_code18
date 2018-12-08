import string
step_reqs = open("../input/day7_input.txt").readlines()


class Letter:
    def __init__(self, step_letter):
        self.letter_char = step_letter
        self.pre_reqs = []


letters_left = []
letter_order = []
letter_dict = {}

for letter in string.ascii_uppercase:
    letters_left.append(letter)
    letter_dict[letter] = Letter(letter)

for step in step_reqs:
    current_letter = None
    for letter in letter_dict.values():
        if step[step.find("before step ") + 11: step.find("can")].strip() == letter.letter_char:
            current_letter = letter
            current_letter.pre_reqs.append(step[step.find("p") + 1: step.find("m")].strip())


def find_next_letter():
    for letter in sorted(letters_left):
        if not letter_dict[letter].pre_reqs:
            letter_order.append(letter)
            letters_left.remove(letter)
            for nletter in letter_dict.values():
                if letter in nletter.pre_reqs:
                    nletter.pre_reqs.remove(letter)
            return


while len(letter_order) < 26:
    find_next_letter()

print(len(letter_order))
for x in letter_order:
    print(x, end='')