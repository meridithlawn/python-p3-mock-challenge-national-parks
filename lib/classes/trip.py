
class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)
        
@property
def visitor(self):
    return self._visitor

@visitor.setter
def visitor(self, visitor):
    if type(visitor) == Visitor:
        self._visitor = visitor
    else:
        raise Exception("must be of type Visitor")

@property
def national_park(self):
    return self._national_park

@national_park.setter
def national_park(self, national_park):
    if type(national_park) == NationalPark:
        self._national_park = national_park
    else:
        raise Exception("must be of type NationalPark")

from classes.visitor import Visitor
from classes.national_park import NationalPark