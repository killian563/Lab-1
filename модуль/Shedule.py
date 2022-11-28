from collections import defaultdict


class Shedule:
    def __init__(self, title):
        self.title = title
        self.timetable = defaultdict(list)

    def print_schedule(self):
        print(self.timetable)