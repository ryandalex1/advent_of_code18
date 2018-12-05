log = [x for x in open("../input/day4_input.txt").readlines()]
log_objects = []


def attr_sort():
    attrs = ['month', 'day', 'hour', 'minute']
    return lambda k: [getattr(k, attr) for attr in attrs]


class LogEntry:
    def __init__(self, line):
        self.month = int(line[6: 8].strip())
        self.day = int(line[9: 11].strip())
        self.hour = int(line[12: 14].strip())
        self.minute = int(line[15: 17].strip())
        try:
            self.guard_number = int(line[line.find("#") + 1: line.find("b")].strip())
            self.falls_asleep = False
            self.wakes_up = False
        except ValueError:
            self.guard_number = 0
            if line[19] == 'f':
                self.falls_asleep = True
                self.wakes_up = False
            else:
                self.falls_asleep = False
                self.wakes_up = True


class Guard:
    def __init__(self, number):
        self.number = number
        self.total_minutes = 0
        self.minutes_dict = {}


for line in log:
    log_objects.append(LogEntry(line))

sorted_log = sorted(log_objects, key=lambda i: (i.month, i.day, i.hour, i.minute))

guards = {}
current_guard = None

time_started_sleeping = 0
for entry in range(0, len(sorted_log)):
    # New guard begins shift
    if sorted_log[entry].guard_number > 0:
        # Seen guard
        if sorted_log[entry].guard_number in guards.keys():
            current_guard = guards[sorted_log[entry].guard_number]
        # Guard never seen before
        else:
            guards[sorted_log[entry].guard_number] = Guard(sorted_log[entry].guard_number)
            current_guard = guards[sorted_log[entry].guard_number]

    if sorted_log[entry].falls_asleep:
        time_started_sleeping = sorted_log[entry].minute

    if sorted_log[entry].wakes_up:
        guards[current_guard.number].total_minutes += sorted_log[entry].minute - time_started_sleeping
        for minute in range(time_started_sleeping, sorted_log[entry].minute):
            if minute in current_guard.minutes_dict.keys():
                current_guard.minutes_dict[minute] += 1
            else:
                current_guard.minutes_dict[minute] = 1


# challenge 1
for guard in guards.values():
    if guard.total_minutes == max([guard.total_minutes for guard in guards.values()]):
        print(guard.number * list(guard.minutes_dict.keys())[list(guard.minutes_dict.values()).index(max(
            guard.minutes_dict.values()))])

# challenge 2
guard_sleep_in_min = {}
for guard in guards.values():
    try:
        guard_sleep_in_min[guard.number] = max(guard.minutes_dict.values())
    except ValueError:
        pass
target_guard = list(guard_sleep_in_min.keys())[list(guard_sleep_in_min.values()).index(max(guard_sleep_in_min.values()))]
for guard in guards.values():
    if guard.number == target_guard:
        target_minute = list(guard.minutes_dict.keys())[list(guard.minutes_dict.values()).index(max(guard.minutes_dict.values()))]
print(target_minute * target_guard)
