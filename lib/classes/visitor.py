class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not (hasattr(self, 'name')) and type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("name must be string between 1-15 characters")
        
    def trips(self):
        return list({trip for trip in Trip.all if trip.visitor == self})
    # return list({order.customer for order in Order.all if order.coffee == self})
    #  return [order for order in Order.all if order.coffee == self]
    def national_parks(self):
        return list({trip.national_park for trip in Trip.all if trip.visitor == self})

from classes.trip import Trip
from classes.national_park import NationalPark