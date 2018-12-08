import string
step_reqs = open("../input/day7_input.txt").readlines()


class Letter:
    def __init__(self, step_letter):
        self.letter_char = step_letter
        self.pre_reqs = []
        self.time = 61 + string.ascii_uppercase.index(self.letter_char)


class Worker:
    def __init__(self):
        self.letter_working_on = None
        self.working = False
        self.time_left = 10000


letters_left = []
letter_order = []
letter_dict = {}
total_time = 0
workers = []

for i in range(5):
    workers.append(Worker())

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
            letters_left.remove(letter)
            return letter
    return None


def letter_completed(letter, worker):
    letter_order.append(letter)
    for nletter in letter_dict.values():
        if letter in nletter.pre_reqs:
            nletter.pre_reqs.remove(letter)
        worker.letter_working_on = None
        worker.time_left = 10000
        worker.working = False


def main_loop():
    global total_time
    for worker in workers:
        if worker.letter_working_on is None:
            worker.letter_working_on = find_next_letter()
            if worker.letter_working_on is not None:
                worker.working = True
                worker.time_left = letter_dict[worker.letter_working_on].time
    min_time = min([worker.time_left for worker in workers])
    total_time += min_time
    for worker in workers:
        worker.time_left -= min_time
        if worker.time_left == 0:
            letter_completed(worker.letter_working_on, worker)


while len(letter_order) < 26:
    main_loop()
    print(total_time)