from collections import deque
from time import time

from .food_item import FoodItem
from .order import Order
from .delivery_system import DeliverySystem

class Restaurant:
    def __init__(self, id: int, total_cooking_slots: int, food_items: list[FoodItem], time_per_km: int, allowed_delivery_time: int):
        self.id = id
        self.total_cooking_slots = total_cooking_slots
        self.food_items = food_items
        self.time_per_km = time_per_km
        self.allowed_delivery_time = allowed_delivery_time
        self.queue = deque()
        self.delivery_system = DeliverySystem(self.total_cooking_slots, self.food_items, self.time_per_km, self.allowed_delivery_time)

    # Number of cooking slots needed for the current order
    def _calculate_cooking_slots(self, order_items: dict):
        cooking_slots = 0
        for order_item, count in order_items.items():
            for food_item in self.food_items:
                if food_item.name == order_item:
                    cooking_slots += food_item.slots_required * count
        return cooking_slots
    
    # Time needed to cook the current order
    def _calculate_cooking_time(self, order_items: dict):
        cooking_time = 0
        for order_item in order_items:
            for food_item in self.food_items:
                if food_item.name == order_item:
                    cooking_time = max(cooking_time, food_item.time_required) # Maximum of cooking time as cooking in slots is simultaneous
        return cooking_time

    # Checking validity of required cooking slots with total cooking slots 
    def _validate_cooking_slots(self, n_slots):
        if n_slots > self.total_cooking_slots:
            raise ValueError('Refused: Cooking slots unavailable')

    def enqueue_order(self, order: Order):
        self.queue.append(order)
        while self.queue:
            if self.queue[0].time_of_receipt + self.queue[0].estimated_delivery_time < order.time_of_receipt:
                self.queue.popleft()
            else:
                break 

    def estimate_order(self, order: Order):
        self.enqueue_order(order)
        cooking_slots_required = self._calculate_cooking_slots(order.items)
        self._validate_cooking_slots(cooking_slots_required)
        cooking_time = self._calculate_cooking_time(order.items)   
        estimated_time = self.delivery_system.calculate_delivery_time(order.time_of_receipt, cooking_slots_required, cooking_time, order.distance)
        order.set_estimated_delivery_time(estimated_time) 
        return estimated_time

    # Get current orders in the queue
    def get_current_orders(self):
        while self.queue:
            print(self.queue[0].time_of_receipt, self.queue[0].estimated_delivery_time)
            if (self.queue[0].time_of_receipt + self.queue[0].estimated_delivery_time) < time()//60:
                self.queue.popleft()
            else:
                break
        return [order.id for order in self.queue]
