class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and not (hasattr(self, "name")):
            self._name = name
        else:
            raise Exception("name must be a string and cannot be changed")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
        # return [trip.start_date for trip in Trip.all if trip.start_date is after now]
    
    def visitors(self):
        return list({trip.visitor for trip in Trip.all if trip.national_park == self})
    
    def total_visits(self):
        total_visits = [trip for trip in Trip.all if trip.national_park == self]
        return len(total_visits)
    
    def best_visitor(self):
        all_visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]
        best = max(set(all_visitors), key = all_visitors.count)
        return best

from classes.trip import Trip
from classes.visitor import Visitor