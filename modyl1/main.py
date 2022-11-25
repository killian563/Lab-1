class Depo:
    def __init__(self):
        self.passenger = Passenger
        self.train = Train


class Train:
    def __init__(self, passengers, maxPassengers):
        self.route = Route
        self.passenger = Passenger
        self.passengers = passengers
        self.maxPassengers = maxPassengers
        self.depo = Depo

    def stop(self):
        if self.route.length_between_depo == 0:
            if self.passenger.final_place == Depo:
                self.passengers -= 1
        if self.depo == Passenger.start_place:
            self.passengers += 1


class Route:
    def __init__(self, length, length_between_depo):
        self.length = length
        self.length_between_depo = length_between_depo
        self.passenger = Passenger


class Passenger:
    def __init__(self, final_place, start_place):
        self.ticket = Ticket
        self.final_place = final_place
        self.start_place = start_place

    def ticket_buyed(self):
        self.ticket.buy_ticket()

    def create_route(self):
        route = self.start_place + self.final_place


class Ticket:
    def __init__(self):
        self.passenger = Passenger
        self.maxtickets = 10000
        self.tickets = 10000
        self.ticket_buyed

    def buy_ticket(self):
        if self.tickets <= self.maxtickets:
            self.tickets -=1
            self.ticket_buyed = 1