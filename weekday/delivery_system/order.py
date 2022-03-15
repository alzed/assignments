from collections import Counter
from time import time

class Order:
    def __init__(self, id:int, items:list, distance:float):
        self._id = id
        self._items = Counter(items) # item -> count mapping
        self._distance = distance
        # Current time in seconds converted to minutes
        self._time_of_receipt = time()//60
        self.estimated_delivery_time = 0
        
    @property
    def id(self):
        return self._id

    @property
    def items(self) -> dict:
        return self._items

    @property
    def distance(self):
        return self._distance

    @property
    def time_of_receipt(self):
        return self._time_of_receipt

    def set_estimated_delivery_time(self, delivery_time):
        self.estimated_delivery_time = delivery_time
