num_of_players = 463
num_of_marbles = 71787
marble_list = [0]
elf_list = []


class Elf:
    def __init__(self):
        self.score = 0


def add_marble(marble):
    if current_marble == marble_list[-1]:
        marble_list.insert(1, marble)
    elif current_marble == marble_list[-2]:
        marble_list.append(marble)
    else:
        marble_list.insert(marble_list.index(current_marble) + 2, marble)


for elf in range(num_of_players):
    elf_list.append(Elf())

current_elf = 0
current_marble = 0
for marble in range(1, num_of_marbles + 1):
    if marble % 23 == 0:
        elf_list[current_elf].score += (marble + marble_list[marble_list.index(current_marble) - 7])
        marble_list.pop(marble_list.index(current_marble)-7)
        current_marble = marble_list[marble_list.index(current_marble)-6]
    else:
        add_marble(marble)
        current_marble = marble

    if current_elf == num_of_players - 1:
        current_elf = 0
    else:
        current_elf += 1

print(max([elf.score for elf in elf_list]))