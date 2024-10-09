
class Schedule:
    def __init__(self, aDate, capacity):
        self.departureDate = aDate
        self.seatsAvailable = self.capacity = capacity

    def bookSeats(self, qty):
        if qty > 0 and self.seatsAvailable - qty >= 0:
            self.seatsAvailable -= qty
            return True
        return False