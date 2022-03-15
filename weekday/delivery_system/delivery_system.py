class DeliverySystem:
    def __init__(self, total_cooking_slots, food_items, time_per_km: int, allowed_delivery_time: int):
        self.total_cooking_slots = total_cooking_slots
        self.food_items = food_items
        self.time_per_km = time_per_km
        self.allowed_delivery_time = allowed_delivery_time

        self.previous_cooking_time = 0
        self.wait_time = 0
        self.available_cooking_slots = self.total_cooking_slots
        self.first_order_time = 0

    # Estimation of travel time by distance
    def _calculate_travel_time(self, distance):
        return distance * self.time_per_km

    # Validation of total delivery time with threshold value
    def _validate_delivery_time(self, delivery_time):
        if delivery_time > self.allowed_delivery_time:
            raise ValueError('Refused: Too long to process order')

    # Updating when cooking slots are filled or are insufficient
    def _update_cooking_availability(self):
        self.available_cooking_slots = self.total_cooking_slots
        self.wait_time += self.previous_cooking_time
        self.previous_cooking_time = 0

    # Modify wait time from order time
    def _modify_wait_time(self, time):
        # Order received after the completion of previous orders
        if self.wait_time > 0 and time >= self.first_order_time + self.wait_time:
            self.wait_time = 0
            self.previous_cooking_time = 0
            self.available_cooking_slots = self.total_cooking_slots
        # Order received in the mid of the inprogress orders
        elif self.wait_time > 0 and time < self.first_order_time + self.wait_time:
            self.wait_time -= time-self.first_order_time
        self.first_order_time = time
               
    def calculate_delivery_time(self, time, cooking_slots_required, cooking_time, distance):
        travel_time = self._calculate_travel_time(distance)
        self._validate_delivery_time(cooking_time + travel_time)
        self._modify_wait_time(time)
        # Insufficient slots
        if cooking_slots_required > self.available_cooking_slots:
            # skipping the current cooking slots and moving to next turn
            total_time = cooking_time + self.wait_time + self.previous_cooking_time + travel_time
            self._validate_delivery_time(total_time)
            # Updating the class variables as a cooking turn is skipped
            self._update_cooking_availability()
        # Slots are available 
        else:
            total_time = cooking_time + self.wait_time + travel_time
            self._validate_delivery_time(total_time)
        # Track cooking time of current cooking turn
        self.previous_cooking_time = max(self.previous_cooking_time, cooking_time)
        self.available_cooking_slots -= cooking_slots_required
        # If cooking slots are filled
        if not self.available_cooking_slots:
            self._update_cooking_availability()
        return total_time
