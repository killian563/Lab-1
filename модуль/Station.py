from abc import abstractmethod


class InfoStation:
    def __init__(self, id: int, title: str, x, y):
        self.id = id
        self.title = title
        self.x = x
        self.y = y


    @abstractmethod
    def personal_manage(self):
        pass


class Station(InfoStation):
    def __init__(self, id: int, title: str, x, y):
        self.id = id
        self.title = title
        self.x = x
        self.y = y
        self.transports = []

    def print_station(self):
        print(self.id, self.title, self.x, self.y)