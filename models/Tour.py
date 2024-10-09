from models.AllTours import AllTours
from models.Schedule import Schedule


class Tour:
    tours = {}

    def __init__(self, code, name, country, cost, description, days, nights, url, schedule):
        self.code = code
        self.name = name
        self.country = country
        self.cost = cost
        self.description = description
        self.days = days
        self.nights = nights
        self.url = url
        self.schedule = []
        for data in schedule:
            self.schedule.append(Schedule(data['departureDate'], data['capacity']))

    @classmethod
    def createTours(cls):
        for data in AllTours.all_Tours:
            cls.tours[data['code']] = Tour(data['code'], data['name'], data['country'], data['cost'],
                                           data['description'], data['days'], data['nights'], data['url'],
                                           data['schedule'])

    @classmethod
    def getAllToursBy(cls, country = None, lower = None, upper= None):
        if not cls.tours:
            cls.createTours()
            lower = 0 if not lower else int(lower)
            upper = 500000 if not upper else int(upper)
        if not country or country.upper() == 'ALL':
            tours = [t for t in cls.tours.values() if lower <= t.cost <= upper]
        else:
            tours = [t for t in cls.tours.values() if lower <= t.cost <= upper and t.country.lower() == country.lower()]
            countries = sorted(list(set([t.country for t in cls.tours.values()])))
        return tours, countries

    @classmethod
    def getTour(cls, code):
        if not cls.tours:
            cls.createTours()
        return cls.tours.get(code)

