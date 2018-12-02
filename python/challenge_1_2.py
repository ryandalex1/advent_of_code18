import csv

total_sum = 0
frequencies_seen = {0}


def cycle_through_input():
    global total_sum
    global frequencies_seen

    with open('../input/1_1_input.csv', newline='') as input_csv:
        sequence_reader = csv.reader(input_csv, dialect='excel')

        for row in sequence_reader:
            total_sum += int(row[0])
            local_sum = total_sum
            local_frequencies = frequencies_seen
            if total_sum in frequencies_seen:
                print(str(total_sum) + " is repeated")
                exit()
            frequencies_seen.add(total_sum)


while True:
    cycle_through_input()